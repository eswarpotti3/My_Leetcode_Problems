class Solution:
    def climbStairs(self, n: int) -> int:
        arr=[0]*(n+2)
        arr[0],arr[1]=0,1
        for i in range(2,n+2):
            # print(arr)
            arr[i]=arr[i-1]+arr[i-2]
        return arr[i]