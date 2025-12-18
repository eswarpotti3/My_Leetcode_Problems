class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        k=[[1]]
        for i in range(numRows-1):
            lis=[1]
            prev=k[i]
            for i in range(len(prev)-1):
                sumi=prev[i]+prev[i+1]
                lis.append(sumi)
            lis.append(1)
            k.append(lis)
        return k
