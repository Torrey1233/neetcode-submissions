class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i in range(len(nums)):
            if target - nums[i] in sum:
                return [sum[target - nums[i]], i]

            sum[nums[i]] = i