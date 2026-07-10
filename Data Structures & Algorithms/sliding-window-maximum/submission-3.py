class Solution:
    import heapq
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []

        # maintain max heap to keep track sorted elements in window
        pq = []
        for i in range(k - 1):
            heapq.heappush(pq, (-nums[i], i))

        l = 0
        r = k - 1
        n = len(nums)

        while r < n:
            # ensure potential max is within window
            while pq and l > pq[0][1]:
                heapq.heappop(pq)

            # remove old max if new element is greater
            if pq and nums[r] > -pq[0][0]:
                heapq.heappop(pq)
            
            # place new element in sorted position
            heapq.heappush(pq, (-nums[r], r))

            # add max to list
            max_list.append(-pq[0][0])

            # slide the fixed window
            r += 1
            l += 1
        
        return max_list

        # T = O(nlgn)
        # S = O(n)