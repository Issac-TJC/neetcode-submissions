class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        left = 0
        right = len(s)-1

        while left < right:
            if not t[left].isalnum():
                left += 1
                continue
            if not t[right].isalnum():
                right -= 1
                continue
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        
        return True
