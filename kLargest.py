import heapq
class KthLargest:
    
    
    def __init__(self, k:int, nums:list[int]):
        
        self.k = k
        heapq.heapify(nums)
        self.min_heap = nums
    
    def add(self, val:int) -> int:
        
        
        '''
        Add incoming value to existing nums array
        Build a max heap from existing 'nums' array
        Pop K-1 times from the heap, then return the root
        '''
        
        heapq.heappush(self.min_heap, val) #O(Log(N))

        #O(NLog(K)) #O(N)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
    
