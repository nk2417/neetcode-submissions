class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        true_order = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in true_order:
                true_order[sorted_word] = []
            true_order[sorted_word].append(word)

        return list(true_order.values())
