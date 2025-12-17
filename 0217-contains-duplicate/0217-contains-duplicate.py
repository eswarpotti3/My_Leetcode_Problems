class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for j in range(len(nums)-1):
                if(nums[j]==nums[j+1]):
                    return True
        return False