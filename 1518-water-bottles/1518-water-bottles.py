class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        sumr=0
        full=numBottles
        ex=numExchange
        new=-1
        empty=full
        sumr=full
        while new!=0:
            new=empty//ex
            sumr+=new
            full=full-(new*ex)
            
            full+=new
            empty=full
            
        return sumr