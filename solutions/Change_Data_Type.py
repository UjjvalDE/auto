class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicates = None
        for num in nums:
            if num in seen:
                duplicates = num
            else:
                seen.add(num)
        res = [duplicates]
        for i in range(1, n+1):
            if i not in seen:
                res.append(i)
        return res