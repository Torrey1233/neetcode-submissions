class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        

        for c in strs:
            count = [0]* 26
            for s in c:
                count[ord(s) - ord("a")] += 1
            results[tuple(count)].append(c)

        return list(results.values())