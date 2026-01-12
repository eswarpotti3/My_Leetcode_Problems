class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        previ, prevj = points[0]
        total_time = 0

        for i, j in points[1:]:
            total_time += max(abs(i - previ), abs(j - prevj))
            previ, prevj = i, j
        return total_time