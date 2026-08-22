from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        seen = set()
        ready_heap = []
        waiting_q = deque()
        counts = Counter(tasks)
        cycles = 0

        for task in tasks:
            if task not in seen:
                heapq.heappush(ready_heap, (-counts[task], task))
                seen.add(task)
        
        while ready_heap or waiting_q:
            if ready_heap:
                curr = heapq.heappop(ready_heap)
                task = curr[1]

                counts[task] -= 1

                if counts[task] != 0:
                    ready_time = cycles + n + 1
                    waiting_q.append((task, ready_time))

            cycles += 1
            while waiting_q and waiting_q[0][1] <= cycles:
                task, ready_time = waiting_q.popleft()
                heapq.heappush(ready_heap, (-counts[task], task))
        
        return cycles
        