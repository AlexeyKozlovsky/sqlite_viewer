from models.enums.compare_operators import CompareOperator


class Condition():
    def __init__(self, column, compare_operator, value):
        self.column = column
        self.compare_operator = compare_operator
        self.value = value
        pass

    def __str__(self):
        return " \"{0}\" {1} {2} ".format(self.column, self.compare_operator,
                                              self.value)
