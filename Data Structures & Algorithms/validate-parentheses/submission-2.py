class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")":"(","]":"[","}":"{"}

        for char in s:
            if char in pair:
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False

        return True
        