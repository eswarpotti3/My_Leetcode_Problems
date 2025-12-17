class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr={}
        for i in range(0,len(nums)):
            
            if target -nums[i] in arr:
                return ( [ arr[target-nums[i]],i])
            arr[nums[i]]=i
        