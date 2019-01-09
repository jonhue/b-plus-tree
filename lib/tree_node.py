from abc import ABC, abstractmethod

class TreeNode(ABC):
    k = 3
    k_leaf = 2

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def lookup(self, hash_key: str, pos: int, key: int):
        pass

    @abstractmethod
    def insert(self, hash_key: str, pos: int, key: int, data):
        pass
