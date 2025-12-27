class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxi=min(height[l],height[r])*abs(l-r)
        while l<r:
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
            k=min(height[l],height[r])*(r-l)
            maxi=max(maxi,k)
        return maxi
        # l,r=height[0],height[len(height)-1]
        # print(l,r)
        # minsave=-99999
        # k=check=0
        # i=0
        # j=len(height)-1
        # while i<j:
        #     if l>=minsave:
        #         k=min(l,r)*(abs(j-i))
        #         if check < k:
        #             check=k
        #             print(check,l,r)
        #         minsave=min(l,r)
        #     i+=1
        #     l=height[i]
        # i=0
        # while not l<j:
        #     if j==0:
        #         break
        #     if l>=minsave:
        #         k=min(l,r)*(abs(j-i))
        #         if check < k:
        #             check=k
        #             print(check,l,r)
        #         minsave=min(l,r)
        #     j-=1
        #     r=height[j]
            
        # return(check)