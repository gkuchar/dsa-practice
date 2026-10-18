class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1

        start_idx, curr_gas = 0, 0
        for i in range(len(gas)):
            curr_gas += gas[i]

            if curr_gas < cost[i]:
                start_idx, curr_gas = i + 1, 0
            else:
                curr_gas -= cost[i]
        
        return start_idx
        # T = O(n)
        # S = O(1)