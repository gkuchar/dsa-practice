class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # stack invariant: top is the slowest car yet to finish.
                   # if the next car ttf (time to finish) is slower, it becomes the head of the next fleet

        cars = dict(zip(position, speed))
        cars = dict(sorted(cars.items(), reverse=True))

        for car_pos, car_speed in cars.items():
            ttf = (target - car_pos) / car_speed
            if not stack or ttf > stack[-1]:
                stack.append(ttf)

        return len(stack)

        # T = O(nlgn)
        # S = O(n)

        