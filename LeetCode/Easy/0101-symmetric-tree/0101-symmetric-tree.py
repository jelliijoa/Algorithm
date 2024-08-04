# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        def check(left, right):
            if left is None and right is None:
                return True
            
            if left is None or right is None:
                return False
            
            return (left.val == right.val) and check(left.right, right.left) and check(left.left, right.right)

        return check(root.left, root.right) if root else True
