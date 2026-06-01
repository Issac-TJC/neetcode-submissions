class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxh = 0
        v = 0
        while l < r:
            cur = min(height[l], height[r])
            add = max(cur-maxh, 0)
            v = v + add * (r-l-1) - min(maxh, cur)
            maxh = cur if cur > maxh else maxh
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return v
        