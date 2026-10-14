class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = {}

        for word in strs:
            ordered = ''.join(sorted(word))
            if ordered not in lists:
                lists[ordered] = []
            lists[ordered].append(word)

        return list(lists.values())