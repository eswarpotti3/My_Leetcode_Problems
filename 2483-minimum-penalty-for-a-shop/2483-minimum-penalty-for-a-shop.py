class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n=len(customers)+1
        prefix=[0]*n
        postfix=[0]*n
        prefix[0]=0
        postfix[n-1]=0
        prev1=prev=0

        for i in range(n-1):
            if customers[i]=="N":
                prefix[i+1]=prefix[i+1-1]+1
            else:
                prefix[i+1]=prefix[i+1-1]
        for i in range(n-2,-1,-1):
            # print(customers[i])
            if customers[i]=="Y":
                # print(postfix,n-i)
                postfix[i]=postfix[i+1]+1
                # print(postfix,"later")
            else:
                postfix[i]=postfix[i+1]
        # print(prefix)
        # print(postfix)
        minsum=99999999
        for i in range(n):
            sum=prefix[i]+postfix[i]
            if minsum>sum:
                # print(minsum,sum,i)
                minsum=sum
                ind=i

        # print(minsum,ind)
        return ind