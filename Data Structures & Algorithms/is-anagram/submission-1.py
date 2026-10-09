class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for i in t:
            count[i] = count.get(i, 0) - 1

        if any(count.values()):
            return False
            
        return True