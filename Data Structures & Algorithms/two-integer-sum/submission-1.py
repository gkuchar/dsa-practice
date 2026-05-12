class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i, num in enumerate(nums):
            if i == 0:
                mapp[num] = 0
                continue
            
            if target - num in mapp:
                vals = [i, mapp[target - num]]
                return sorted(vals)
            
            mapp[num] = i
        
        # T = O(n)
        # S = O(n)