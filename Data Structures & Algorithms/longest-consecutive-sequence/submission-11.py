class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 

        for i in nums:
            if (i-1) not in numSet:
                y = 0
                while (i+y) in numSet:
                    y +=1 
                    longest = max(longest,y)

        return longest
        