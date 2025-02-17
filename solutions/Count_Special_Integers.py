class Solution:
    def specialInteger(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            if i == (n - i):
                count += 1
        return count