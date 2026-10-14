class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        real_order = {}

        for word in strs:
            ordered_word = ''.join(sorted(word))
            if ordered_word not in real_order:
                real_order[ordered_word] = []
            
            real_order[ordered_word].append(word)

        return list(real_order.values())
