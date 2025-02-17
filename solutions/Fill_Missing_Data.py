class Solution:
    def getMissingList(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1, n2 = len(nums1), len(nums2)
        set1, set2 = set(nums1), set(nums2)
        missing = sorted(list(set1.symmetric_difference(set2)))
        return missing