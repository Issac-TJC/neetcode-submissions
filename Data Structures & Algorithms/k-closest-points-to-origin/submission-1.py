class Point:
    def __init__(self, point):
        self.point = point
        self.val = math.sqrt(point[0]**2 + point[1]**2)
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # minheap 每次插入都是nlogm（m是之前插入的，所以如果允许的话，弹出再插入可以减少复杂度）
        # 可以用maxheap来限制heap容量为k，maxheap只要取-val就可以实现
        minHeap = []
        for point in points:
            heapq.heappush(minHeap, Point(point))

        res = []
        for _ in range(k):
            if minHeap:
                cur = heapq.heappop(minHeap)
                res.append(cur.point)
        return res
        