from .leaf_node import LeafNode
from .tree_node import TreeNode

class Tree:
    def __init__(self, k: int, k_leaf: int):
        TreeNode.k = k
        TreeNode.k_leaf = k_leaf
        self.root_node = LeafNode(self)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.root_node)

    def lookup(self, key: int):
        return self.root_node.lookup(key)

    def rangelookup(self, start: int, end: int):
        return self.root_node.rangelookup(start, end)

    def insert(self, key: int, data):
        return self.root_node.insert(key, data)
