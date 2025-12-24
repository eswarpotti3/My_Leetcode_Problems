class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sumi=sum(apple)
        ind=0
        capacity.sort(reverse=True)
        i=0
        while sumi>0:
            ind+=1
            sumi-=capacity[i]
            i+=1
            # print(sumi)
        return ind