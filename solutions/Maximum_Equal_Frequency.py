def maxEqualFrequency(nums):
    frequency = {}
    for num in nums:
        if num not in frequency:
            frequency[num] = 0
        frequency[num] += 1

    max_count = 0
    max_equal_frequency = 0

    for key, value in frequency.items():
        equal_frequency = list(frequency.values()).count(value)
        if equal_frequency > 0 and value > max_count:
            max_count = value
            max_equal_frequency = equal_frequency

    return max_equal_frequency * max_count