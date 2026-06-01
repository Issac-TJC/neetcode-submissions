class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse=True)
        l = 1
        r = piles[0]
        while l < r:
            mid = l + (r-l) // 2
            t = 0
            for i in range(len(piles)):
                if piles[i] <= mid:
                    t += (len(piles)-i)
                    break
                t += math.ceil(piles[i] / mid)
            if t <= h:
                r = mid
            else:
                l = mid + 1
        return l
