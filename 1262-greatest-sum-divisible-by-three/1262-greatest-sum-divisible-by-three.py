class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)

        if total % 3 == 0:
            return total

        rem1 = []
        rem2 = []

        for x in nums:
            if x % 3 == 1:
                rem1.append(x)
            elif x % 3 == 2:
                rem2.append(x)

        rem1.sort()
        rem2.sort()

        if total % 3 == 1:
            candidates = []
            if len(rem1) >= 1:
                candidates.append(total - rem1[0])
            if len(rem2) >= 2:
                candidates.append(total - rem2[0] - rem2[1])
            return max(candidates) if candidates else 0

        if total % 3 == 2:
            candidates = []
            if len(rem2) >= 1:
                candidates.append(total - rem2[0])
            if len(rem1) >= 2:
                candidates.append(total - rem1[0] - rem1[1])
            return max(candidates) if candidates else 0
