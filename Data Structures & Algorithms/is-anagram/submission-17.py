class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def word_count(n):
            count = {}

            for c in n:
                if c not in count:
                    count[c] = 1
                else:
                    count[c] += 1
            return count

        return word_count(s) == word_count(t)
        