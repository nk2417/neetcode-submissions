class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        def word_count(n):
            count = {}
            for char in n:
                if char not in count:
                    count[char] = 1
                else:
                    count[char] += 1

            return count

        return word_count(s) == word_count(t)