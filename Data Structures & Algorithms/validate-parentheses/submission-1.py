class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == "]":
                if not stack or stack[-1] != "[":
                    return False
                else:
                    stack.pop()
            if char == "}":
                if not stack or stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            if char == ")":
                if not stack or stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
        
        if stack:
            return False

        return True
            