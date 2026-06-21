class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) >= 2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            c = a - b
            if c != 0:
                heapq.heappush(stones, c)
        if stones:
            return -stones[0]
        else:
            return 0
        