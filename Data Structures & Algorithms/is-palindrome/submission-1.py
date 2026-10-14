class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = "".join(char.lower() for char in s if char.isalnum())
        L = 0
        R = len(pal) - 1
        while L < R:
            if pal[R] != pal[L]:
                return False
            L += 1
            R -= 1

        
        return True
