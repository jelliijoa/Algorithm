class Solution(object):
    def generate(self, numRows):
        pascal = []

        for i in range(numRows):
            # pascal [[1], [1, 1], [1, 2, 1]]
            # i = 3 / row [1, 1, 1, 1]
            row = [1] * (i + 1)

            for j in range(1, i):
                # j = 1, 2
                # j = 1 -> pascal[2][0] + pascal[2][1] -> row [1, 3, 1, 1]
                # j = 2 -> pascal[2][1] + pascal[2][2] -> row[1, 3, 3, 1]
                row[j] = pascal[i-1][j-1] + pascal[i-1][j]

            pascal.append(row)
        
        return pascal