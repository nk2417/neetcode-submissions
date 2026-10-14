class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in values:
                return [values[complement], i]
            else:
                values[n] = i
        return []
