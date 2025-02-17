class Solution:
    def largeGroupPhrases(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
                count += 1
            if count >= 3:
                res.append(s[:i+1] + s[i+1:])
            else:
                res.append(s[:i+1])
            i += count
        return [''.join(g) for g in itertools.groupby(res, str)]