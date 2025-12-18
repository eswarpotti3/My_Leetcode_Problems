class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0:
            return -1
        i=1
        remain=0
        while i<k+1:
            remain=(remain*10+1)%k
            if remain==0:
                return i
            # print(i,remain)
            i+=1
        
