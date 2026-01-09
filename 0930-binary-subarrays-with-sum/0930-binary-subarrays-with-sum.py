class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(x):
            if x<0:return 0
            i,cur=0,0
            res=0
            for j in range(len(nums)):
                cur+=nums[j]
                while cur>x:
                    cur-=nums[i]
                    i+=1
                res+=(j-i+1)
            return res
        return helper(goal)-helper(goal-1)