class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        new = []

        for i in range(len(arr)):
            if i + 1 < len(arr):
                new.append(max(arr[i+1:]))
            else:
                new.append(-1)

        return new
            
        