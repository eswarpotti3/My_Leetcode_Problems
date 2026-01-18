class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1 and len(matrix[0])==1:
            if matrix[0][0]==target:
                return True
            return False
        m=len(matrix)-1
        n=len(matrix[0])-1
        
        l=0

        while l<=m:
            if matrix[l][0]<=target and target<=matrix[l][n]:
                if matrix[l][0]==target or target==matrix[l][n]:
                    return True
                for i in range(n+1):
                    if matrix[l][i]==target:
                        return True
                return False
            else:
                l+=1

