class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(key=lambda x:x[0],reverse=True)
        pleets = len(position)
        stack = [0]
        for p,s in pair:
            t = (target-p)/s
            if t <= stack[-1]:
                pleets -= 1
            else:
                stack.append(t)
        return pleets
