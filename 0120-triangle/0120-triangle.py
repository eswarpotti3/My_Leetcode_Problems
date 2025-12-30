class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-2,-1,-1):
    
            m=len(triangle[i])
            # print(triangle[i],m)
            for j in range(m):
                left=triangle[i+1][j]
                right=triangle[i+1][j+1]
                # print(triangle[i][j]+min(left,right),left,right)
                triangle[i][j]+=min(left,right)
        return triangle[0][0]