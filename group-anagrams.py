class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        results = []
        for word in strs:
            sort_w = tuple(sorted(word))
            if sort_w not in ans:
                ans[sort_w] = [word]
            else:
                ans[sort_w].append(word)
        for k in ans:
            results.append(ans[k])
           
        return results