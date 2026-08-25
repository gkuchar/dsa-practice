import heapq
class MedianFinder:

    # maintain 2 heaps to actively keep track of the midpoint
    # the two heaps should be at most different in length by 1 element
    # S = O(n), n = len(numbers in dtaa stream)
    def __init__(self):
        # max heap to store all values at or less than midpoint
        # max heap gives fast access to closest number smaller or equal to midpoint
        self.low = []

        # min heap to store all values greater than midpoint
        # min heap gives fast access to closest number greater or equal to midpoint
        self.high = []

    # T = O(lgn)
    def addNum(self, num: int) -> None:
        if not self.low:
            heapq.heappush(self.low, -num)
        elif num >= -self.low[0]:
            # num greater than or equal to midpoint, place into high heap
            heapq.heappush(self.high, num)

            # rebalance only if the lengths differ by 2
            # since just added to high, the smallest high needs to join low
            if len(self.high) > len(self.low) + 1:
                high_top = heapq.heappop(self.high)
                heapq.heappush(self.low, -high_top)
        else:
            # num is less than midpoint, add to low
            heapq.heappush(self.low, -num)

            # rebalance only if the lengths differ by 2
            # since just added to low, largest low must join high
            if len(self.low) > len(self.high) + 1:
                low_top = -heapq.heappop(self.low)
                heapq.heappush(self.high, low_top)
        
    # T = O(1)
    def findMedian(self) -> float:
        # even total count requires averaging
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        elif len(self.low) > len(self.high):
            return float(-self.low[0])
        else:
            return float(self.high[0])

        