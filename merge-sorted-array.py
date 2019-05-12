class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        l = len(nums1) - len(nums2) - 1
        for i in range(len(nums2)):
            while nums2[i] > nums1[j] and j <= l:
                j += 1
            n = nums2[i]
            l += 1
            for k in range(j, len(nums1)):
                n, nums1[k] = nums1[k], n
        
            