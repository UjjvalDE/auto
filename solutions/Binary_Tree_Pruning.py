# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if not root.left and not root.right:
            return None
        elif not (root.left or root.right):
            return root.val != 0 and TreeNode(root.val) or None
        
        return root