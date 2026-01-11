class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(x):
            if x<0: return 0
            res=0
            i=0
            cur=0
            for j in range(len(nums)):
                cur+=nums[j]%2
                while cur>x:
                    cur-=nums[i]%2
                    i+=1
                res+=(j-i+1)
            return res
        return helper(k)-helper(k-1)