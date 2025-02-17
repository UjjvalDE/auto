def minimizeAddParenthesis(expression):
    n = len(expression)
    dp = [[0, 0] for _ in range(n + 1)]
    for i in range(1, n):
        if expression[i - 1] == '(':
            dp[i][0] = dp[i - 1][0] + 1
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
        else:
            dp[i][0] = max(0, dp[i - 1][0] - 1)
            dp[i][1] = max(0, dp[i - 1][1] - 1) if i < n and expression[i] == ')' else dp[i - 1][1]
    return (dp[n - 1][0] + dp[n - 1][1]) // 2 if expression[0] == '(' else max(0, dp[0][1])