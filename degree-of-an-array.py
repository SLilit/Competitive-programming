class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        right = {}
        left = {}
        max_d = 0
        min_l = float("inf")
        for i in range(len(nums)):
            n = nums[i]
            if n not in count:
                count[n] = 1
                right[n] = left[n] = i
            else:
                count[n] += 1
                right[n] = i
            if count[n] > max_d:
                #print('1: ', count[n], right[n], left[n])
                max_d = count[n]
                min_l = right[n] - left[n] + 1
            elif count[n] == max_d and (right[n] - left[n] + 1) < min_l :
                #print('2: ', count[n], right[n], left[n])
                min_l = right[n] - left[n] + 1
            
        return min_l
                