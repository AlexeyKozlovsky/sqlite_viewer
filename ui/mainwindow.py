# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1075, 585)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1044, 516))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.orRadioButton = QRadioButton(self.layoutWidget)
        self.orRadioButton.setObjectName(u"orRadioButton")

        self.gridLayout.addWidget(self.orRadioButton, 7, 3, 1, 1)

        self.addConditionButton = QPushButton(self.layoutWidget)
        self.addConditionButton.setObjectName(u"addConditionButton")

        self.gridLayout.addWidget(self.addConditionButton, 3, 7, 1, 2)

        self.removeFromDBButton = QPushButton(self.layoutWidget)
        self.removeFromDBButton.setObjectName(u"removeFromDBButton")

        self.gridLayout.addWidget(self.removeFromDBButton, 8, 1, 1, 1)

        self.andRadioButton = QRadioButton(self.layoutWidget)
        self.andRadioButton.setObjectName(u"andRadioButton")

        self.gridLayout.addWidget(self.andRadioButton, 7, 4, 1, 1)

        self.searchByQueryButton = QPushButton(self.layoutWidget)
        self.searchByQueryButton.setObjectName(u"searchByQueryButton")

        self.gridLayout.addWidget(self.searchByQueryButton, 1, 7, 1, 2)

        self.addToConditionsComboBoxButton = QPushButton(self.layoutWidget)
        self.addToConditionsComboBoxButton.setObjectName(u"addToConditionsComboBoxButton")

        self.gridLayout.addWidget(self.addToConditionsComboBoxButton, 7, 5, 1, 1)

        self.allConditionsListWidget = QListWidget(self.layoutWidget)
        self.allConditionsListWidget.setObjectName(u"allConditionsListWidget")

        self.gridLayout.addWidget(self.allConditionsListWidget, 5, 3, 1, 3)

        self.resultTableWidget = QTableWidget(self.layoutWidget)
        self.resultTableWidget.setObjectName(u"resultTableWidget")

        self.gridLayout.addWidget(self.resultTableWidget, 0, 2, 8, 1)

        self.AddToDBButton = QPushButton(self.layoutWidget)
        self.AddToDBButton.setObjectName(u"AddToDBButton")

        self.gridLayout.addWidget(self.AddToDBButton, 8, 0, 1, 1)

        self.mainTableWidget = QTableWidget(self.layoutWidget)
        self.mainTableWidget.setObjectName(u"mainTableWidget")

        self.gridLayout.addWidget(self.mainTableWidget, 0, 0, 8, 2)

        self.openButton = QPushButton(self.layoutWidget)
        self.openButton.setObjectName(u"openButton")

        self.gridLayout.addWidget(self.openButton, 9, 0, 1, 3)

        self.resultConditionsListWidget = QListWidget(self.layoutWidget)
        self.resultConditionsListWidget.setObjectName(u"resultConditionsListWidget")

        self.gridLayout.addWidget(self.resultConditionsListWidget, 5, 6, 1, 3)

        self.searchByConditionsButton = QPushButton(self.layoutWidget)
        self.searchByConditionsButton.setObjectName(u"searchByConditionsButton")

        self.gridLayout.addWidget(self.searchByConditionsButton, 7, 7, 1, 2)

        self.queryTextWidget = QTextEdit(self.layoutWidget)
        self.queryTextWidget.setObjectName(u"queryTextWidget")

        self.gridLayout.addWidget(self.queryTextWidget, 0, 3, 1, 6)

        self.removeFromDBButton2 = QPushButton(self.layoutWidget)
        self.removeFromDBButton2.setObjectName(u"removeFromDBButton2")

        self.gridLayout.addWidget(self.removeFromDBButton2, 8, 2, 1, 1)

        self.selectColumnComboBox = QComboBox(self.layoutWidget)
        self.selectColumnComboBox.setObjectName(u"selectColumnComboBox")

        self.gridLayout.addWidget(self.selectColumnComboBox, 3, 3, 1, 2)

        self.selectOperatorComboBox = QComboBox(self.layoutWidget)
        self.selectOperatorComboBox.addItem("")
        self.selectOperatorComboBox.addItem("")
        self.selectOperatorComboBox.addItem("")
        self.selectOperatorComboBox.addItem("")
        self.selectOperatorComboBox.addItem("")
        self.selectOperatorComboBox.setObjectName(u"selectOperatorComboBox")

        self.gridLayout.addWidget(self.selectOperatorComboBox, 3, 5, 1, 1)

        self.selectValueLine = QLineEdit(self.layoutWidget)
        self.selectValueLine.setObjectName(u"selectValueLine")
        self.selectValueLine.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.selectValueLine, 3, 6, 1, 1)

        self.removeFromResultConditionsButton = QPushButton(self.layoutWidget)
        self.removeFromResultConditionsButton.setObjectName(u"removeFromResultConditionsButton")

        self.gridLayout.addWidget(self.removeFromResultConditionsButton, 7, 6, 1, 1)

        self.showQueryButton = QPushButton(self.layoutWidget)
        self.showQueryButton.setObjectName(u"showQueryButton")

        self.gridLayout.addWidget(self.showQueryButton, 8, 6, 1, 3)

        self.clearQueryTextButton = QPushButton(self.layoutWidget)
        self.clearQueryTextButton.setObjectName(u"clearQueryTextButton")

        self.gridLayout.addWidget(self.clearQueryTextButton, 1, 6, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1075, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.orRadioButton.setText(QCoreApplication.translate("MainWindow", u"OR", None))
        self.addConditionButton.setText(QCoreApplication.translate("MainWindow", u"Add condition", None))
        self.removeFromDBButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.andRadioButton.setText(QCoreApplication.translate("MainWindow", u"AND", None))
        self.searchByQueryButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.addToConditionsComboBoxButton.setText(QCoreApplication.translate("MainWindow", u"->", None))
        self.AddToDBButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.openButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.searchByConditionsButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.queryTextWidget.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.removeFromDBButton2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.selectOperatorComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"=", None))
        self.selectOperatorComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u">", None))
        self.selectOperatorComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u">=", None))
        self.selectOperatorComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"<", None))
        self.selectOperatorComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"<=", None))

        self.removeFromResultConditionsButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.showQueryButton.setText(QCoreApplication.translate("MainWindow", u" Show query", None))
        self.clearQueryTextButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

