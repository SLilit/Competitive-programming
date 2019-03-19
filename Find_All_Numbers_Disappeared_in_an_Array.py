class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d_nums = []
        l = len(nums) + 1
        nums = set(nums)
        for i in range(1,l):
            if i not in nums:
                d_nums.append(i)
        
        return d_nums

        return list(set(range(1,len(nums)+1)) - set(nums))