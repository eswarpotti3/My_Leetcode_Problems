class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxsum=arr[0]
        cursum=0
        for n in arr:
            if cursum<0:
                cursum=0
            cursum+=n
            maxsum=max(cursum,maxsum)
        return maxsum


        # maxsum=max(arr)
        # for k in range(2,len(arr)+1): 
        #     sum=0
        #     for i in range(k):
        #         sum+=arr[i]
        #     j=0
        #     if sum>maxsum:
        #         maxsum=sum
        #     for i in range(k,len(arr)):
        #         sum+=arr[i]
        #         sum-=arr[j] 
        #         j+=1
        #         if sum>maxsum:
        #             maxsum=sum
        # return maxsum
