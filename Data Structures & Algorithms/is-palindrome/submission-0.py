class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = s.lower()
        left = 0
        right = len(s)-1

        while left < right:
            while left < right and not t[left].isalnum():
                left += 1
            while left < right and not t[right].isalnum():
                right -= 1
            if t[left] != t[right]:
                return False
            left += 1
            right -= 1
        
        return True
