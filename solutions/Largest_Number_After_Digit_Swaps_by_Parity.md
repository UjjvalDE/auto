# Largest Number After Digit Swaps by Parity

**Problem Link:** [https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity](https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity)

## Solution

Here is the Python solution for the "Largest Number After Digit Swaps by Parity" problem on LeetCode:
```
def largestNumberAfterDigitsSwaps(nums):
    def get_digits(num):
        return [int(d) for d in str(num)]

    def swap(p1, p2):
        if p1 < p2:
            p1, p2 = p2, p1
        return p2

    digits = []
    for num in nums:
        digits.extend(get_digits(num))
    sorted_digits = sorted(set(digits), reverse=True)
    parity_counts = {0: 0, 1: 0}
    swaps = 0
    for digit in sorted_digits:
        if digit % 2 == 0:
            parity_counts[0] += 1
        else:
            parity_counts[1] += 1

    while True:
        swap_count = 0
        for i, digit in enumerate(digits):
            p = int(str(digit) % 2)
            if p != parity_counts[p]:
                j = len(digits) - 1
                while j > i and int(str(digits[j]) % 2) == p:
                    j -= 1
                digits[i], digits[j] = digits[j], digits[i]
                swap_count += 1
        if swap_count == 0:
            break

    return ''.join(map(str, digits))
```
This code uses a helper function `get_digits` to extract the individual digits from each input number. The main function `largestNumberAfterDigitsSwaps` first sorts all the digits in descending order and counts the parity of each digit. Then it iteratively swaps the odd and even digits until they match the desired parity, and finally returns the resulting largest number as a string.