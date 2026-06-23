class Point:
    def __init__(self, point):
        self.point = point
        self.val = math.sqrt(point[0]**2 + point[1]**2)
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for point in points:
            heapq.heappush(minHeap, Point(point))

        res = []
        for _ in range(k):
            if minHeap:
                cur = heapq.heappop(minHeap)
                res.append(cur.point)
        return res
        