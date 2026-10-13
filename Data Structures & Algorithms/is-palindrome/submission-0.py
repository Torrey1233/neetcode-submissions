class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""

        for char in s:
            if char.isalnum():
                pal += char.lower()
                
        left = 0
        right = len(pal) - 1
        while left < right:
            if pal[left] != pal[right]:
                return False
            
            
            left += 1
            right -= 1
         
                
        
        return True
            
            
            

            