class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        subsums = {0:1}
        s = 0
        
        for n in nums:
            s += n
            if s - k in subsums:
                count += subsums[s-k]
            if s in subsums:
                subsums[s] += 1
            else:
                subsums[s] = 1
        return count

                    
        