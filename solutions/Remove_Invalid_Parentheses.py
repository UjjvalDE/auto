def removeInvalidParentheses(s):
    if not s:
        return []

    n = 0
    res = []
    for c in s:
        if c == '(':
            if n > 0:
                res.append(c)
            else:
                n += 1
        elif c == ')':
            if n < 0:
                res.append(c)
                n -= 1
            elif n == 0:
                continue
            else:
                res.append(c)
                n -= 1
    return res