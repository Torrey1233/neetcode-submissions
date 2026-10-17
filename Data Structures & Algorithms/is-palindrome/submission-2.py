class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
       
        for letter in s:
            if letter.isalnum():
                pal += letter.lower()
            
        
        L = 0
        R = len(pal) - 1
        #tabacat
        while L <= R:
            if pal[L] != pal[R]:
                return False
            else:
                L += 1
                R -= 1
        return True