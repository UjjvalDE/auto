class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_score = 0
        left, right = 0, k
        total = sum(nums[:k+1])
        
        while right < n:
            total -= nums[left]
            left += 1
            if right + 1 < n: 
                total += nums[right+1]
            right += 1
            
            max_score = max(max_score, total)
        
        return max_score