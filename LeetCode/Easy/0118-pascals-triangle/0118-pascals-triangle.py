from math import comb

class Solution(object):
    def generate(self, numRows: int) -> List[List[int]]:
        return [[comb(n, k) for k in range(n + 1)] for n in range(numRows)]