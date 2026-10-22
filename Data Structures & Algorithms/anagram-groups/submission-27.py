class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered = {}

        for s in strs:
            ordere = "".join(sorted(s))
            if ordere not in ordered:
                ordered[ordere] = []
            ordered[ordere].append(s)
        
        return list(ordered.values())
            
        