class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in s:
            count[i] = count.get(i, 0) + 1
        for j in t:
            count[j] = count.get(j, 0) - 1
        return all(value == 0 for value in count.values())
        return False
