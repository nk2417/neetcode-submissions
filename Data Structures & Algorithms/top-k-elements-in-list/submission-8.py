class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums)+1)]
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
            bucket[value].append(key)
        
        for i in range(len(bucket) -1, 0, -1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result

