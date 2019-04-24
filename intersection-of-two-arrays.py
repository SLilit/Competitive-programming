class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def inter(A,B):
            
            result = []
            for a in A:
                if a in B:
                    result.append(a)
            return result
            
        n1 = set(nums1)
        n2 = set(nums2)
        if len(n1) > len(n2):
            return inter(n1, n2)
        return inter(n2, n1)



        n1 = set(nums1)
        n2 = set(nums2)
        
        return list(set.intersection(n1,n2))