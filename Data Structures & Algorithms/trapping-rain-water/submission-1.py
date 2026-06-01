class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxh = 0
        v = 0
        while l < r:
            cur = min(height[l], height[r])
            if cur > maxh:
                v = v + (cur-maxh)*(r-l-1) - maxh
                maxh = cur
            else:
                v -= cur
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return v
        