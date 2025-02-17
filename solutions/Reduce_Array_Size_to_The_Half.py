def minCount(nums):
    nums.sort()
    res = 0
    i, n = 0, len(nums)
    while i < n:
        res += 1
        i += 1
        if i * 2 > n:
            break
        i *= 2
    return res