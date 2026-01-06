class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # i=0
        goal=len(nums)-1
        for i in range(goal,-1,-1):
            print(i,nums[i])
            if i+nums[i]>=goal:
                print(i,nums[i],goal)
                goal=i
                print(goal)
        if goal==0:
            return True
        return False