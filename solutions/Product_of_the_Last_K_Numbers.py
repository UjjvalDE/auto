class Solution:
    def productOfNumbers(self, nums):
        res = [1] * (len(nums) + 1)
        for i in range(len(nums)):
            res[i + 1] = nums[i] * res[i]
        while res[-1] == 0:
            res.pop()
        return str(res[-1]) if len(res) > 1 else '0'