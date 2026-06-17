class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l = 0
        r = n - 1

        def bs(arr, l, r, t):
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == t:
                    return mid
                elif arr[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1
            
            return -1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        min_i = r
        print(f'min index: {min_i}')

        if min_i == 0: # one, non-broken section
            print('whole')
            return bs(nums, 0, n - 1, target)
        elif target >= nums[0]: # first section
            print('first')
            return bs(nums, 0, min_i - 1, target)
        else: # second section
            print('second')
            return bs(nums, min_i, n - 1, target)
        
        # T = O(lgn)
        # S = O(1)
