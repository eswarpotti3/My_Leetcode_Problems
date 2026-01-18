class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][n-1]:
                l,r = 0, n-1

                while l <= r:
                    m = (l+r)//2
                    if target == matrix[i][m]:
                        return True
                    elif target <= matrix[i][m]:
                        r = m-1
                    else:
                        l = m+1
                return False
        return False
        