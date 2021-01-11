from models.condition import Condition
from models.enums.operator import Operator
from models.exceptions.condition_chain_error import ConditionChainError


class ConditionChain():
    def __init__(self):
        self.conditions = []
        self.operators = []

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current > len(self.conditions):
            raise StopIteration
        elif self.current % 2 == 0:
            return self.conditions[self.current // 2]
        else:
            return self.operators[self.current // 2]

    def __str__(self):
        result = ""
        for i in range(len(self.conditions) + len(self.operators)):
            result += str(self.conditions[i // 2]) if i % 2 == 0 else str(self.operators[i // 2])

        return result

    def addCondition(self, condition, operator=None):
        if not isinstance(condition, Condition):
            raise ValueError

        if operator != None and not isinstance(operator, Operator):
            raise ValueError

        if len(self.conditions) != 0 and operator == None:
            raise ConditionChainError

        self.conditions.append(condition)
        if len(self.conditions) == 1:
            return

        self.operators.append(operator) if operator != None else None

    def removeCondition(self):
        if len(self.conditions) == 0:
            raise IndexError

        del self.conditions[-1]
        if len(self.conditions) != 0:
            del self.operators[-1]

    def popCondition(self, index):
        if index < 0 or index >= len(self.conditions):
            raise IndexError

        self.conditions.pop(index)
        if not self.operators:
            return

        if index > 0:
            self.operators.pop(index - 1)
        else:
            self.operators.pop(index)
