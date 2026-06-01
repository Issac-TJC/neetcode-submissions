class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 1
        long = 1
        while l < r < len(s):
            # split may cause o(n^2) while searching
            # use dict to record last seen
            if s[r] in s[l:r]:
                long = max(r-l,long)
                while s[l] != s[r]:
                    l += 1
                l += 1
            r += 1
        long = max(r-l,long)
        return long
        