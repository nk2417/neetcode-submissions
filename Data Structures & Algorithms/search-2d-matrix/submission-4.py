class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(x, target):
            l, r = 0, len(x) - 1

            while l <= r:
                m = (l+r) // 2
                if x[m] > target:
                    r = m -1
                elif x[m] < target:
                    l = m + 1
                else:
                    return True
            return False

        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l+r) // 2

            if matrix[m][0] > target:
                r = m -1 
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                return binary(matrix[m], target)

        return False