class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        values = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            values[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            values[i] *= postfix
            postfix *= nums[i]
        
        return values