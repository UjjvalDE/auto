def canBeSorted(nums):
    count = [0] * 26
    
    for num in nums:
        count[num - ord('a')] += 1
    
    if sum(i % 2 for i in count) > 1:
        return False
    
    return True