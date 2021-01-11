from enum import Enum


class Operator(Enum):
    OR = 0
    AND = 1

    def __str__(self):
        if self.value == 0:
            return "or"
        else:
            return "and"
