class ConditionChainError(Exception):
    def __init__(self):
        super().__init__("Error in forming condition chain")

    def __init__(self, message):
        super().__init__(message)
