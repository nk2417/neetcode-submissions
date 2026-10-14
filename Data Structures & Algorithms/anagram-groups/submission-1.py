class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        true = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in true:
                true[sorted_word] = []
            true[sorted_word].append(word)

        return list(true.values())
            