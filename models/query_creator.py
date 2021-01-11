from models.condition import Condition
from models.condition_chain import ConditionChain


class QueryCreator():
    def createQuery(conditionChain, tableName):
        if not conditionChain.conditions:
            return ""
        return "select * from {0}\nwhere{1}".format(tableName, conditionChain)
