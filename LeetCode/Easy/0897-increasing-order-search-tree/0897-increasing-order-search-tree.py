class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
        
class Solution(object):
    def increasingBST(self, root):
        inorder = []

        def in_order(node):
            if node:
                in_order(node.left)
                inorder.append(node.val)
                in_order(node.right)

        in_order(root)
        
        root = TreeNode(inorder[0])
        cur = root
        for val in inorder[1:]:
            cur.right = TreeNode(val)
            cur = cur.right
        
        return root