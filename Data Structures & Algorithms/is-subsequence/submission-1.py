class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # how many chars of s we've matched so far
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)
        