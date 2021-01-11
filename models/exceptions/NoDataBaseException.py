class NoDataBaseException(Exception):
    def __init__(self):
        super().__init__("Data base has not been found")
