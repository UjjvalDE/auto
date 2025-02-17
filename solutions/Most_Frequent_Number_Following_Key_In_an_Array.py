class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n = len(nums)
        count = {}
        for i in range(n-1):
            if nums[i] == key:
                num = nums[i+1]
                count[num] = count.get(num, 0) + 1
        return max(count, key=count.get)