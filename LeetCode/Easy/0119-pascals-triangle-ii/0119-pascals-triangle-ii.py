class Solution(object):
    def getRow(self, rowIndex):
        row = [1]
        
        for k in range(1, rowIndex + 1):
            # C(n, k) = C(n, k-1) * (n-k+1/k)
            row.append(row[k - 1] * (rowIndex - k + 1) // k)
        
        return row