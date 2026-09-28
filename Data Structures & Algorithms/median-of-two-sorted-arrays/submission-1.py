class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        master = sorted(nums1)
        n = len(master)
        if n % 2 == 0:
            return (master[n // 2] + master[n // 2 - 1]) / 2
        else:
            return master[n // 2]