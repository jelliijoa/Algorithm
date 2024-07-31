import heapq

# minheap
# val이 add 될 때마다 k번째로 큰 값 찾기
# heap 크기를 k로 유지하면 minheap일 때 heap[0]이 k번째로 큰 값

# ex : [4, 5, 8, 2], 3, 5, 10, 9, 4 (k = 3)

class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.heap = []
        
        for n in nums:
            self.add(n)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
            
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, val)
        
        return self.heap[0]

    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)