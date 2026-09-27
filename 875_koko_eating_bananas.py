class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_num = max(piles)
        left = 1
        right = max_num

        def hours_needed(speed):
            return sum(math.ceil(pile / speed) for pile in piles)

        while left <= right:
            mid = (left + right) // 2
            hours = hours_needed(mid)
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left


