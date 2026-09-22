class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows = len(matrix)-1
        while rows>-1:
            if matrix[rows][0]>target:
                rows-=1
            elif matrix[rows][0]<=target:
                for i in range(len(matrix[rows])):
                    if matrix[rows][i]==target:
                        return True
                return False
        return False