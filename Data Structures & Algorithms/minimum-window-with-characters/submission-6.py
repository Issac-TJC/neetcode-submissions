class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = {}
        need = len(t)
        size = len(s)
        l = 0
        res = ""
        for i in t:
            mp[i] = 1 + mp.get(i, 0)
        for r in range(len(s)):
            if need == 0:
                if (r - l) < size:
                    size = r - l
                    res = s[l:r]
            if s[r] in mp:
                if mp[s[r]] <= 0:
                    mp[s[r]] -= 1
                    # while s[l] not in mp or s[l] == s[r] or mp[s[l]] < 0:
                    #     l += 1
                    #     if s[l] in mp and mp[s[l]] < 0:
                    #         mp[s[l]] += 1
                    while l < r:
                        # if s[l] == s[r] and mp[s[l]] < 0:
                        #     mp[s[l]] += 1
                        # elif s[l] in mp and s[l] != s[r]:
                        #     break
                        # elif s[l] == s[r] and mp[s[l]] == 0:
                        #     break
                        if s[l] in mp and mp[s[l]] < 0:
                            mp[s[l]] += 1
                        elif s[l] in mp and mp[s[l]] >= 0:
                            break
                        l += 1
                else:
                    while l < r and s[l] not in mp:
                        l += 1
                    mp[s[r]] -= 1
                    need -= 1
        if need == 0:
            if (r - l) < size:
                    size = r - l
                    res = s[l:r+1]
        return res
