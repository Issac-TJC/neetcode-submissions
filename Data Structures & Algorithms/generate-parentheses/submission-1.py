class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def backtrack(i, stack, cnt):
            if i == 2 * n:
                res.append("".join(cur))
                return
            if stack == 0:
                cur.append("(") 
                backtrack(i + 1, stack + 1, cnt + 1)
                cur.pop()
            elif cnt == n:
                cur.append(")")
                backtrack(i + 1, stack - 1, cnt)
                cur.pop()
            else:
                cur.append("(")
                backtrack(i + 1, stack + 1, cnt + 1)
                cur.pop()
                cur.append(")")
                backtrack(i + 1, stack - 1, cnt)
                cur.pop()
        
        backtrack(0, 0, 0)
        return res
            
        