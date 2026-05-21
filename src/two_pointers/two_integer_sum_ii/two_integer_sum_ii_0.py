class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        if n == 2: return [1,2]

        l = 0
        r = n - 1

        while True:
            summ = numbers[l] + numbers[r]
            if summ == target: return [l + 1, r + 1]

            if summ > target:
                r -= 1
            else:
                l += 1

        # T = O(n)
        # S = O(1)