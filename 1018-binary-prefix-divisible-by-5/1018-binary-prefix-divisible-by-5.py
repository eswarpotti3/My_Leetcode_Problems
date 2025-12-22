class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n=len(nums)
        res=[False]*n
        s=''
        for i in range(len(nums)):
            s+=str(nums[i])
            number=int(s,2)
            if number%5==0:
                res[i]=True
        return res