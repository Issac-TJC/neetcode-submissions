class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = list(s)
        chart = list(t)

        mps = {}
        mpt = {}

        for char in chars:
            if char in mps:
                mps[char] += 1
            else:
                mps[char] = 1
        
        for char in chart:
            if char in mpt:
                mpt[char] += 1
            else:
                mpt[char] = 1
        
        # for char in mps:
        #     if char not in mpt or mps[char] != mpt[char]:
        #         return False
        
        # for char in mpt:
        #     if char not in mps:
        #         return False
        
        # return True

        return mps == mpt