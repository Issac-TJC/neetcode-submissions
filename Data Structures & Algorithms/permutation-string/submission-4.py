class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = {}
        for s in s1:
            mp[s] = 1 + mp.get(s,0)
        l = 0
        need = len(s1)
        for r in range(len(s2)):
            # if all(v == 0 for v in mp.values()):
            #     return True
            if need == 0:
                return True
            elif s2[r] in mp:
                mp[s2[r]] -= 1
                need -= 1
                if mp[s2[r]] < 0:
                    while s2[l] != s2[r]:
                        if s2[l] in mp:
                            mp[s2[l]] += 1
                            need += 1
                        l += 1
                    mp[s2[r]] += 1
                    need += 1
                    l += 1
            # elif all(v == 0 for v in mp.values()):
            #     return True
            else:
                while l < r:
                    if s2[l] in mp:
                        mp[s2[l]] += 1
                        need += 1
                    l += 1
        # if all(v == 0 for v in mp.values()):
        #     return True    
        if need == 0:
                return True   
        return False
