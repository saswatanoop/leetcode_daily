# https://leetcode.com/problems/create-binary-tree-from-descriptions/?envType=daily-question&envId=2026-06-07


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # T:O(n)
        tree_node_map={} #value->TreeNode
        is_node_child=set() #all children are added here       
        
        for parent,child,isLeft in descriptions:
            if parent not in tree_node_map:
                tree_node_map[parent]=TreeNode(parent)
            if child not in tree_node_map:
                tree_node_map[child]=TreeNode(child)
            is_node_child.add(child)
            if isLeft:
                tree_node_map[parent].left=tree_node_map[child]
            else:
                tree_node_map[parent].right=tree_node_map[child]
        
        for k in tree_node_map:
            if k not in is_node_child:
                return tree_node_map[k]