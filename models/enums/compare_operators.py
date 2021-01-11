from enum import Enum


class CompareOperator(Enum):
    EQUAL = 0
    MORE = 1
    MORE_AND_EQUAL = 2
    LESS = 3
    LESS_AND_EQUAL = 4

    def __str__(self):
        if self.value == 0:
            return "="
        elif self.value == 1:
            return ">"
        elif self.value == 2:
            return ">="
        elif self.value == 3:
            return "<"
        else:
            return "<="
