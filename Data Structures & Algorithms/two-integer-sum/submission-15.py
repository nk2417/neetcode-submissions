class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for k, v in enumerate(nums):
            complement = target - v
            if complement in values:
                return [values[complement], k]
            values[v] = k
        
        return []

        