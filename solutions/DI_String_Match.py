class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        left, right = 0, len(s)
        res = []
        
        for c in s:
            if c == 'I':
                res.append(left)
                left += 1
            else:
                res.append(right - 1)
                right -= 1
                
        return [left, *res, right]