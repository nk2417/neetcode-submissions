class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1 
    
        for num, freq in count.items():
            bucket[freq].append(num)

        res = []

        for i in range(len(bucket) - 1,0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


        

