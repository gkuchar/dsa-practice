import heapq
class MedianFinder:

    def __init__(self):
        # all values at or less than midpoint (max heap)
        self.low = []

        # all values greater than midpoint (min heap)
        self.high = []
        

    def addNum(self, num: int) -> None:
        # print(f'adding: {num}')
        if not self.low:
            # print('first element')
            heapq.heappush(self.low, -num)
        elif num >= -self.low[0]:
            # print(f'{num} >= {-self.low[0]} ')
            heapq.heappush(self.high, num)

            if len(self.high) > len(self.low) + 1:
                high_top = heapq.heappop(self.high)
                heapq.heappush(self.low, -high_top)
        else:
            heapq.heappush(self.low, -num)

            if len(self.low) > len(self.high) + 1:
                low_top = -heapq.heappop(self.low)
                heapq.heappush(self.high, low_top)

        # print(f'low: {self.low}')
        # print(f'high: {self.high}')

        

    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (-self.low[0] + self.high[0]) / 2
        elif len(self.low) > len(self.high):
            return float(-self.low[0])
        else:
            return float(self.high[0])

        