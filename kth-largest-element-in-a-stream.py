class KthLargest:

     import heapq
    
    def __init__(self, k: int, nums: List[int]):
       
        self.k = k
        self.nums = sorted(nums)
        self.heap = self.nums[-self.k:]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            
        elif val >= self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
            
        return self.heap[0]



    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)
        self.klargest = self.nums[-self.k:]

    def add(self, val: int) -> int:
        if len(self.klargest) < self.k:
            self.klargest.append(val)
            self.klargest = sorted(self.klargest)
        elif val > self.klargest[0]:
            self.klargest[0] = val
            self.klargest = sorted(self.klargest)
            
        if len(self.klargest) < self.k:
            return None
        return self.klargest[0]
                 


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)