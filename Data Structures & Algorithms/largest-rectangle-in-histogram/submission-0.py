class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [0]
        heights.append(0)
        largest = 0
        for i,h in enumerate(heights):
            if h > heights[stack[-1]]:
                stack.append(i)
                continue
            elif h == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
                continue
            while stack and h < heights[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = stack[-1] + 1
                else:
                    left = 0
                largest = max(largest, (i-left)*heights[mid])
            stack.append(i)
        return largest
        