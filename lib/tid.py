class TID:
    def __init__(self, key: int, data):
        self.key = key
        self.data = data

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '<' + str(self.key) + ',' + str(self.data) + '>'
