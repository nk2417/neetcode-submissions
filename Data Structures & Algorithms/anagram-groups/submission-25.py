class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        true_order = {}

        for w in strs:
            ordered = "".join(sorted(w))
            if ordered not in true_order:
                true_order[ordered] = []
            true_order[ordered].append(w)

        return list(true_order.values())
       