class Solution:
    def countVowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        dp = [[0] * (5 if w == '' else w.count('a') + 1) for w in words]
        
        for i, word in enumerate(words):
            if not word:
                dp[i][1] = 1
            else:
                prev = dp[i - 1][dp[i].index(1)]
                dp[i][0] = (dp[i-1][0] + prev) % MOD
                for j in range(1, len(word)):
                    if word[j] not in 'aeiou':
                        break
                    dp[i][j+1] += prev
                    dp[i][j+1] %= MOD
        
        return [((dp[q[0]][q[1]] + sum(dp[j][min(q[2], i)] for j in range(max(0, q[1]-1), min(len(words), q[1]+2))) - 
                 (dp[max(0, q[1]-1)][q[1]] if q[1] > 0 else dp[q[0]][0]) + 
                 (dp[min(len(words)-1, q[1]+1)][min(q[2], len(words) - 1)] if q[1] < len(words) - 1 else dp[-1][4])) % MOD for q in queries]