class Solution:
    def minimumDeviation(self, nums):
        n = len(nums)
        nums.sort()
        left, right = 1, n
        while True:
            if (target := min((a := nums[i-1]) * b for i, b in enumerate(range(left, right+1), 1))) % b == 0:
                return target
            if a > target // b:
                break
            left += 1
        for r in range(right, 0, -1):
            if (t := min((a := nums[i-1]) * b for i, b in enumerate(range(left, r+1), 1))) % b == 0:
                return t
            if a > t // b:
                break
        return -1