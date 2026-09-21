class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        # cur = ""

        def backtrack(i, cur, stack, cnt):
            if i == 2 * n:
                res.append(cur)
                return
            if stack == 0:
                cur += "("
                cnt += 1
                stack += 1
                backtrack(i + 1, cur, stack, cnt)
            elif cnt == n:
                cur += ")"
                stack -= 1
                backtrack(i + 1, cur, stack, cnt)
            else:
                cur += "("
                cnt += 1
                stack += 1
                backtrack(i + 1, cur, stack, cnt)
                cur = cur[:-1]
                stack -= 1
                cnt -= 1
                cur += ")"
                stack -= 1
                backtrack(i + 1, cur, stack, cnt)
        
        backtrack(0, "", 0, 0)
        return res
            
        