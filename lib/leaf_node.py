from typing import List

from .tid import TID
from .internal_node import InternalNode
from .tree_node import TreeNode

class LeafNode(TreeNode):
    def __init__(self, parent_node, data: List[TID] = [], next_leaf = None):
        self.parent_node = parent_node
        self.data = data
        self.next_leaf = next_leaf

    def __str__(self):
        return '<LeafNode data=' + str(self.data) + '>'

    def lookup(self, key: int):
        for tid in self.data:
            if tid.key == key:
                return tid.data

    def insert(self, key: int, data):
        self.data.append(TID(key, data))
        if len(self.data) <= 2 * TreeNode.k_leaf:
            self.data = sorted(self.data, key=lambda tid: tid.key)
        elif isinstance(self.parent_node, InternalNode):
            self._resolve_to_next_node()
        else:
            self._create_root_node()

    def _create_root_node(self):
        left_leaf, right_leaf = self._split()
        node = InternalNode(self.parent_node, [left_leaf, right_leaf], [left_leaf.data[len(left_leaf.data) - 1].key])
        left_leaf.parent_node = node
        right_leaf.parent_node = node
        self.parent_node.root_node = node

    def _resolve_to_next_node(self):
        left_leaf, right_leaf = self._split()
        self.parent_node.resolve(left_leaf.data[len(left_leaf.data) - 1].key, left_leaf, right_leaf)

    def _split(self):
        right_leaf = LeafNode(self.parent_node, self.data[len(self.data)//2:], self.next_leaf)
        left_leaf = LeafNode(self.parent_node, self.data[:len(self.data)//2], right_leaf)
        return left_leaf, right_leaf
