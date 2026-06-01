class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {'+':0,'-':0,'*':1,'/':1}

        i = 0

        while i < len(tokens):
            if tokens[i] not in op:
                stack.append(int(tokens[i]))
                i += 1
                continue
            if tokens[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tokens[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif tokens[i] == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
            i += 1
        
        return stack.pop()
        