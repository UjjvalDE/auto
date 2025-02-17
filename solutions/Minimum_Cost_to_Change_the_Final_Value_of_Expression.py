def finalValueAfterXTurns(n, x):
    res = 0
    while x:
        if x & 1:
            res += 1
        x >>= 1
    return n - (1 << res)