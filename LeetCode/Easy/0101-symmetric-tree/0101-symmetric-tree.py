# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        
        stack = [(root.left, root.right)]

        while stack:
            left, right = stack.pop()

            # 양쪽 모두 없으면 대칭
            if not left and not right:
                continue
            
            # left, right 중 하나만 존재하면 or 양쪽 값이 다르면 비대칭
            if (not left or not right) or (left.val != right.val):
                return False
            
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))

        return True