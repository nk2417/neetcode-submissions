class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}

        for key, value in enumerate(nums):
            complement = target - value
            if complement in values:
                return [values[complement], key]
            values[value] = key

        return []