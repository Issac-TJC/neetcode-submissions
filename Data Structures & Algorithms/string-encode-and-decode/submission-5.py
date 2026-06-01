class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for s1 in strs:
            s += str(len(s1))
            s += ","
            for char in s1:
                s += char
            # s += "#"
        return s

    def decode(self, s: str) -> List[str]:
        l = list(s)
        l1 = []
        t = ""
        size = ""
        i = 0
        while i < len(l):
            char = l[i]
            if char == ",":
                for j in range(i+1,i+int(size)+1):
                    t += s[j]
                l1.append(t)
                i = i + int(size) + 1
                size = ""
                t = ""
            else:
                size += char
                i += 1
        return l1
