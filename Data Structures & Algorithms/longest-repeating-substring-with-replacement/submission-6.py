class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        maxf = 0
        long = 0
        mp = {}
        mp[s[l]] = 1 + mp.get(s[l], 0)
        while l < r < len(s):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxf = max(maxf, mp[s[r]])
            if (r - l + 1 - maxf) > k:
                long = max(long, r - l)
                mp[s[l]] -= 1
                l += 1
            r += 1
        long = max(long, r - l)
        return long
        