class Solution:
    def addBinary(self, a: str, b: str) -> str:
        first=a 
        last=b 
        i=0
        string=""
        carry=0
        lenfirst=len(first)
        lenlast=len(last)
        if (lenfirst>lenlast):
            st="0"*(lenfirst-lenlast)
            last=st+last
        if (lenfirst<lenlast):
            st="0"*(lenlast-lenfirst)
            first=st+first
        # print(first,last)
        first=first[::-1]
        last=last[::-1]
        while i<len(first) and i<len(last):
            k=int(first[i])+int(last[i])+carry
            if k==2:
                carry=1
                k=0
            elif k==3:
                carry=1
                k=1
            else:carry=0
            string+=str(k)
            i+=1
        if carry==1:
            string+=str(carry)
        return string[::-1]