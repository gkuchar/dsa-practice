class Solution:
    import heapq
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_list = []
        pq = []
        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))
        #print(f'pq_init: {pq}')

        l = 0
        r = k - 1
        n = len(nums)

        while r < n:
            while pq and l > pq[0][1]:
               #print(f'max out of window. l = {l}, max_i = {pq[0][1]}')
                heapq.heappop(pq)

            #print(f'pq before max_check: {pq}')
            if pq and nums[r] > -pq[0][0]:
                heapq.heappop(pq)
            
            heapq.heappush(pq, (-nums[r], r))
            #print(f'pq after max_check: {pq}')

            max_list.append(-pq[0][0])
            #print(f'window: {nums[l:r+1]}, max = {-pq[0][0]}, max_list = {max_list}')

            r += 1
            l += 1
        
        return max_list