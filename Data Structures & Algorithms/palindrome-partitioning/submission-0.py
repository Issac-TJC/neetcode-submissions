class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def is_pali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l += 1
                    r -= 1
            return True
        
        def backtrack(i):
            if i == len(s):
                res.append(cur.copy())
                return
            for j in range(i, len(s)):
                if is_pali(i, j):
                    cur.append(s[i: j + 1])
                    backtrack(j + 1)
                    cur.pop()

        backtrack(0)
        return res
