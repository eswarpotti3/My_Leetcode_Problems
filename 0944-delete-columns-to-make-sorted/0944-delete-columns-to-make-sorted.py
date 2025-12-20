class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        abc="abcdefghijklmnopqrstuvwxyz"
        count=0
        n=len(strs[0])
        k=["a"]*n
        # print(k)
        # for i in strs:
        #     print(i)
        for i in strs:
            for j in range(len(i)):
                # print(j,k[j],i[j],k,count)
                if k[j]=='aa':
                    continue
                if  i[j]<k[j]:
                    # print(k[j],i[j],k)
                    k[j]="aa"
                    count+=1
                else:
                    k[j]=i[j]
            
        return count