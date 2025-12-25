class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        # print(happiness)
        sumi=0

        for i in range(k):
            # print(happiness[i]-i)
            if happiness[i]-i>0:
                sumi+=happiness[i]-i
            else:
                break
        return sumi
