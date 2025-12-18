class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def each(n):
            a=n
            while n>0:
                re=n%10
                if re==0:
                    return False
                print(n)
                if a%re!=0:
                    return False
                n=n//10
            return True

        # each(13)
        res=[]
        
        if left<=9 and right >10:
            for i in range(left,10):
                res.append(i)
            for i in range(11,right+1):
                if each(i):
                    print(res)
                    res.append(i)
        else:
            for i in range(left,right+1):
                if each(i):
                    print(res)
                    res.append(i)
        return res