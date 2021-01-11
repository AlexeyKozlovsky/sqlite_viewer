import sys

from PySide2 import QtWidgets
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData, Table

from ui import mainwindow
from models.condition import Condition
from models.enums.operator import Operator
from models.condition_chain import ConditionChain
from models.enums.compare_operators import CompareOperator
from models.exceptions.NoDataBaseException import NoDataBaseException
from models.query_creator import QueryCreator


class MainWindow(mainwindow.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.orRadioButton.setChecked(True)
        self.orRadioButton.setEnabled(False)
        self.andRadioButton.setEnabled(False)
        self.AddToDBButton.setEnabled(False)
        self.removeFromDBButton.setEnabled(False)
        self.removeFromDBButton2.setEnabled(False)


        self.conditionChain = ConditionChain()
        self.conditions = []
        self.columnTypes = []
        self.engine = None
        self.session = None
        self.table = None


        self.initSignals()
        self.initActions()

    def initSignals(self):
        self.openButton.clicked.connect(self.openDb)
        self.searchByQueryButton.clicked.connect(self.executeSqlQueryByText)
        self.addConditionButton.clicked.connect(self.addCondition)
        self.addToConditionsComboBoxButton.clicked.connect(self.chooseCondition)
        self.removeFromResultConditionsButton.clicked.connect(self.removeFromChosenCondition)
        self.selectColumnComboBox.currentIndexChanged.connect(self.updateOperatorComboBox)
        self.showQueryButton.clicked.connect(self.showQuery)
        self.clearQueryTextButton.clicked.connect(self.clearQuery)
        self.searchByConditionsButton.clicked.connect(self.searchByConditions)

    def initActions(self):
        self.actionExit.triggered.connect(sys.exit)
        self.actionOpen.triggered.connect(self.openDb)

    def initColumnKeysComboBox(self):
        if self.table == None:
            raise NoDataBaseException

        for key in self.table.columns.keys():
            self.selectColumnComboBox.addItem(str(key))

    def updateOperatorComboBox(self):
        if self.table == None:
            return

        currentColumn = self.selectColumnComboBox.currentIndex()
        operatorsCount = self.selectOperatorComboBox.count()

        if not str(self.columnTypes[currentColumn]).startswith("VARCHAR"):
            for i in range(operatorsCount):
                self.selectOperatorComboBox.model().item(i).setEnabled(True)
        else:
            self.selectOperatorComboBox.setCurrentIndex(0)
            for i in range(1, operatorsCount):
                self.selectOperatorComboBox.model().item(i).setEnabled(False)

    def showQuery(self):
        if not self.conditionChain or self.table == None:
            return

        query = QueryCreator.createQuery(self.conditionChain, self.table.name)
        self.queryTextWidget.setText(query)

    def clearQuery(self):
        self.queryTextWidget.setText("")

    def addCondition(self):
        if self.table == None:
            return

        columnStr = self.selectColumnComboBox.currentText()
        compareOperatorStr = self.selectOperatorComboBox.currentText()
        valueStr = self.selectValueLine.text()

        currentIndex = self.selectColumnComboBox.currentIndex()
        if str(self.columnTypes[currentIndex]).startswith("VARCHAR"):
            valueStr = "\"{0}\"".format(valueStr)

        condition = Condition(columnStr, compareOperatorStr, valueStr)


        self.conditions.append(condition)
        self.allConditionsListWidget.addItem(str(condition))

        self.selectValueLine.setText("")

    def chooseCondition(self):
        if not self.conditions or self.table == None:
            return

        selectedConditionIndex = self.allConditionsListWidget.currentRow()
        currentCondition = self.conditions[selectedConditionIndex]
        currentOperator = Operator.OR if self.orRadioButton.isChecked() else Operator.AND
        self.conditionChain.addCondition(currentCondition, currentOperator)

        self.resultConditionsListWidget.addItem(str(currentCondition))

        self.orRadioButton.setEnabled(True)
        self.andRadioButton.setEnabled(True)

        print(str(self.conditionChain))
        query = QueryCreator.createQuery(self.conditionChain, self.table.name)
        print(query)
        self.executeSqlQueryByConditions(query)

    def removeFromChosenCondition(self):
        selectedIndex = self.resultConditionsListWidget.currentRow()
        if selectedIndex == -1:
            return

        self.resultConditionsListWidget.model().removeRow(selectedIndex)
        self.conditionChain.popCondition(selectedIndex)

        query = QueryCreator.createQuery(self.conditionChain, self.table.name)
        print(query)
        self.executeSqlQueryByConditions(query)

        if not self.conditionChain.conditions:
            self.orRadioButton.setEnabled(False)
            self.andRadioButton.setEnabled(False)




    def initMainTableWidget(self):
        if self.table == None or self.engine == None:
            raise NoDataBaseException

        columnKeys = self.table.columns.keys()
        columnsCount = len(columnKeys)

        self.mainTableWidget.setColumnCount(columnsCount)
        self.mainTableWidget.setHorizontalHeaderLabels(columnKeys)
        self.resultTableWidget.setColumnCount(columnsCount)
        self.resultTableWidget.setHorizontalHeaderLabels(columnKeys)
        rowsCount = self.mainTableWidget.rowCount()

        data = self.session.query(self.table).all()
        for rowNumber, row in enumerate(data):
            self.mainTableWidget.insertRow(rowNumber)
            for columnNumber, value in enumerate(row):
                cell = QtWidgets.QTableWidgetItem(str(value))
                self.mainTableWidget.setItem(rowNumber, columnNumber, cell)


    def initResultTableWidget(self, data):
        self.resultTableWidget.setRowCount(0)

        for rowNumber, row in enumerate(data):
            self.resultTableWidget.insertRow(rowNumber)
            for columnNumber, value in enumerate(row):
                cell = QtWidgets.QTableWidgetItem(str(value))
                self.resultTableWidget.setItem(rowNumber, columnNumber, cell)



    def openDb(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, "Open DB",
                                                         "","*.db")[0]
        engineName = "sqlite:///{0}".format(fileName)
        self.engine = create_engine(engineName, echo=True)
        engine = self.engine
        Session = sessionmaker(bind=engine)
        self.session = Session()

        with engine.connect() as connection:
            result = connection.execute("select * from students")
            for row in result:
                print(row)

        self.meta = MetaData()
        self.meta.reflect(bind=engine)

        self.table = Table(self.meta.sorted_tables[0], self.meta, autoload=True,
                       autoload_with=engine)

        self.columnTypes = []
        for column in self.table.columns:
            self.columnTypes.append(column.type)
        print(self.columnTypes)

        self.initMainTableWidget()
        self.initColumnKeysComboBox()

    def addToDb(self):
        # Не успел пока разобраться, как реализовать

        if self.table == None:
            raise NoDataBaseException

    def removeFromDb(self):
        # Не успел пока разобраться, как реализовать

        if self.table == None:
            raise NoDataBaseException

        currentIndex = self.mainTableWidget.currentRow()
        currentObj = self.engine.execute("select * from {0} where id = {1}".format(
            self.table.name, currentIndex
        ))
        self.session.delete(currentObj)
        self.session.commit()
        self.initMainTableWidget()


    def executeSqlQueryByText(self):
        if self.table == None:
            return

        query = self.queryTextWidget.toPlainText()
        if query == "":
            return

        data = self.engine.execute(query)
        self.initResultTableWidget(data)

    def searchByConditions(self):
        if self.table == None:
            return

        query = QueryCreator.createQuery(self.conditionChain, self.table.name)
        self.executeSqlQueryByConditions(query)


    def executeSqlQueryByConditions(self, query):
        print(query)
        if self.table == None or not self.conditionChain:
            return

        if query == "":
            self.resultTableWidget.setRowCount(0)
            return

        data = self.engine.execute(query)
        self.initResultTableWidget(data)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()
    sys.exit(0)
