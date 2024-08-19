class Solution(object):
    def missingNumber(self, nums):
        for i, v in enumerate(sorted(nums)):
            if i != v:
                return i
        return len(nums)