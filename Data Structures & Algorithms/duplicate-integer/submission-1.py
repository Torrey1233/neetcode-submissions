class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for x in nums:
            if x in duplicate:
                return True
            duplicate[x] = True
        return False

        