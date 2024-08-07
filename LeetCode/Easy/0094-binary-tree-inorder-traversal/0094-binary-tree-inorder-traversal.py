# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    # left root right
    def inorderTraversal(self, root):
        inorder = []

        def in_order(node):
            if node:
                in_order(node.left)
                inorder.append(node.val)
                in_order(node.right)

        in_order(root)
        
        return inorder