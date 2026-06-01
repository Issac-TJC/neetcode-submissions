class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            cur = temperatures[i]
            while stack != [] and cur > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = i-prev
            stack.append(i)
        return res
        