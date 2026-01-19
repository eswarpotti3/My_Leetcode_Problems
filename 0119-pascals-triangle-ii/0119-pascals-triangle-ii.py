class Solution:
    def getRow(self, numRows: int) -> List[int]:
        # numRows = 1
        k=[[1]]
        for i in range(numRows):
            lis=[1]
            prev=k[i]
            for i in range(len(prev)-1):
                sumi=prev[i]+prev[i+1]
                lis.append(sumi)
            lis.append(1)
            k.append(lis)
        return k[-1]