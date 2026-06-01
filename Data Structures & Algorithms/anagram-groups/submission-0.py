class Solution:
    def is_anag(self, str1: str, str2:str):
        if len(str1) != len(str2):
            return False

        counts1 = {}
        counts2 = {}

        for i in range(0, len(str1)):
            counts1[str1[i]] = 1 + counts1.get(str1[i],0)
            counts2[str2[i]] = 1 + counts2.get(str2[i],0)
        
        return counts1 == counts2

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = [0]*len(strs)
        rlt = []

        for i in range(0, len(strs)):
            if anags[i] != 0:
                continue
            anags[i] = 1
            now = []
            now.append(strs[i])
            for j in range(i+1, len(strs)):
                if anags[j] != 0:
                    continue
                if self.is_anag(strs[i], strs[j]):
                    anags[j] = 1
                    now.append(strs[j])
            rlt.append(now)

        return rlt
