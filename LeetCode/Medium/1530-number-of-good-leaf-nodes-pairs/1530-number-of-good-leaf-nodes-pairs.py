class Solution(object):
    def countPairs(self, root, distance):
        
        self.result = 0
        
        def dfs(node):
            if not node:
                return []
            
            if not node.left and not node.right:
                return [1]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            for l in left:
                for r in right:
                    if l + r <= distance:
                        self.result += 1
            
            return [d + 1 for d in left + right if d + 1 < distance]
        
        dfs(root)
        
        return self.result