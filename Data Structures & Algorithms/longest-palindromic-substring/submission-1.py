class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pali(l, r):
            while l >=0 and r < len(s):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            return r - l - 1
            

        res = s[0]
        longest = 1
        for i in range(1, len(s)):
            a = is_pali(i, i)
            b = is_pali(i, i - 1)
            if a > longest:
                longest = a
                res = s[i - a // 2:i + a // 2 + 1]
            if b > longest:
                longest = b
                res = s[i - b // 2:i + b // 2]
        return res  

        