class Solution:
    def shortestToTarget(self, s: str, target: str) -> List[int]:
        res = []
        for i in range(len(s)):
            if s[i] == target[0]:
                res.append(i)
            else:
                res.append(-abs(i - len(target)))
        return res