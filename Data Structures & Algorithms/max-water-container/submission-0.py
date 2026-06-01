class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxV = 0
        while l < r:
            cur = min(heights[l],heights[r])*(r-l)
            maxV = max(maxV, cur)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maxV
        