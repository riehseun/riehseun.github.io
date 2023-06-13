from heapq import heappush, heappop

class MedianFinder:

    # Use min heap and max heap
    # min heap stores larger numbers
    # max heap stores smaller numbers

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heappush(self.max_heap, -num)
            root = -heappop(self.max_heap)
            heappush(self.min_heap, root)
        else:
            heappush(self.min_heap, num)
            root = heappop(self.min_heap)
            heappush(self.max_heap, -root)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0]-self.max_heap[0])/2.0
        else:
            return self.min_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()