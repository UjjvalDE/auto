class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        target_sum = total_sum // 3
        parts = 0
        current_sum = 0
        for num in arr:
            current_sum += num
            if current_sum == target_sum:
                parts += 1
                current_sum = 0
        return parts >= 3