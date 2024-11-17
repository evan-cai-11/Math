import heapq

class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, x: int):
        max_left = self.maxHeap[0] if len(self.maxHeap) > 0 else -x
        min_right = self.minHeap[0] if len(self.minHeap) > 0 else x

        if (x <= -max_left):
            if len(self.minHeap) >= len(self.maxHeap):
                heapq.heappush(self.maxHeap, -x)
            else:
                max_left = heapq.heapreplace(self.maxHeap, -x)
                heapq.heappush(self.minHeap, -max_left)
        elif (x >= min_right):
            if len(self.maxHeap) >= len(self.minHeap):
                heapq.heappush(self.minHeap, x)
            else:
                min_right = heapq.heapreplace(self.minHeap, x)
                heapq.heappush(self.maxHeap, -min_right)
        else:
            if len(self.minHeap) >= len(self.maxHeap):
                heapq.heappush(self.maxHeap, -x)
            else:
                heapq.heappush(self.minHeap, x)


    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return -self.maxHeap[0]

sol = Solution()
sol.addNum(1)
sol.addNum(2)
print(sol.findMedian())
sol.addNum(3)
print(sol.findMedian())
sol.addNum(4)
print(sol.findMedian())
sol.addNum(-1)
print(sol.findMedian(), sol.minHeap, list(map(lambda x: -x, sol.maxHeap)))