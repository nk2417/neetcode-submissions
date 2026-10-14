class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] * 2 * len(nums)
         
        
        for i in range(2):
            for n in nums:
                ans.append(n)
        return ans

                

        