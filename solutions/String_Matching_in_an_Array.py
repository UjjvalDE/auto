class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for w1 in words:
            for w2 in words:
                if w1 != w2 and w1 in w2:
                    result.append(w1)
                    break
        return list(set(result))