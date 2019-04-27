class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        left = {}
        max_d = 0
        min_l = float("inf")
        for i in range(len(nums)):
            n = nums[i]
            if n not in count:
                count[n] = 1
                left[n] = i
            else:
                count[n] += 1
            if count[n] > max_d:
                max_d = count[n]
                min_l = i - left[n] + 1
            elif count[n] == max_d:
                min_l = min(min_l,i - left[n] + 1)
            
        return min_l
                