class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(x, y):
            l = 0
            r = len(x) - 1
            while l <= r:
                mid = (l+r) // 2
                if x[mid] < y:
                    l = mid + 1
                elif x[mid] > y:
                    r = mid - 1
                else:
                    return True
            return False 
            
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = (l+r) // 2
            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                return binary(matrix[mid], target)
        return False
       