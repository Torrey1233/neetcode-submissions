class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        #for i, frequency in count:
        sort = sorted(
            count.items(),
            key = lambda item: item[1],
            reverse = True
        )
        for i, frequency in sort[0:k]:
            result.append(i)
        return result