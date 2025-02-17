class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        i = 0
        while i < n - 2:
            if arr[i] >= arr[i+1]:
                i += 1
                continue
            j = i + 1
            while j < n-1 and arr[j] < arr[j+1]:
                j += 1
            k = j
            while k < n - 1 and arr[k] > arr[k+1]:
                k += 1
            res = max(res, k-i+1)
            i = k + 1
        return res