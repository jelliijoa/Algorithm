class Solution(object):
    def arrayPairSum(self, nums):
        nums = sorted(nums)
        return sum(nums[i] for i in range(0, len(nums)-1, 2))