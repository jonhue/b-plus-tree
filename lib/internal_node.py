from typing import List

from .tree_node import TreeNode

class InternalNode(TreeNode):
    def __init__(self, parent_node, child_nodes: List[TreeNode] = [], references: List[int] = []):
        self.parent_node = parent_node
        self.child_nodes = child_nodes
        self.references = references

    def __str__(self):
        return '<InternalNode child_nodes=' + str(self.child_nodes) + ', references=' + str(self.references) + '>'

    def lookup(self, key: int):
        self._find_child_node(key).lookup(key)

    def insert(self, key: int, data):
        self._find_child_node(key).insert(key, data)

    def resolve(self, reference, left_child_node, right_child_node):
        if len(self.references) < 2 * TreeNode.k:
            i = self._find_child_node_index(reference)
            self.references.insert(i, reference)
            self.child_nodes[i] = left_child_node
            self.child_nodes.insert(i + 1, right_child_node)
        else:
            left_node = InternalNode(self.parent_node, self.child_nodes[:len(self.child_nodes)//2], self.references[:len(self.references)//2][:-1])
            right_node = InternalNode(self.parent_node, self.child_nodes[len(self.child_nodes)//2:], self.references[len(self.references)//2:])
            if isinstance(self.parent_node, InternalNode):
                print(self.references[round(len(self.references)/2)])
                self.parent_node.resolve(self.references[round(len(self.references)/2)], left_node, right_node)
            else:
                node = InternalNode(self.parent_node, [left_node, right_node], [self.references[round(len(self.references)/2)]])
                left_node.parent_node = node
                right_node.parent_node = node
                self.parent_node.root_node = node

    def _find_child_node(self, key):
        return self.child_nodes[self._find_child_node_index(key)]

    def _find_child_node_index(self, key):
        if key <= self.references[0]:
            return 0

        # Do this with binary search
        i = 0
        for reference in self.references:
            if key <= reference:
                break
            i += 1
        return i
