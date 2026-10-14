class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        true_order = {}

        for strings in strs:
            order = "".join(sorted(strings))
            if order not in true_order:
                true_order[order] = []
            true_order[order].append(strings)

        return list(true_order.values())