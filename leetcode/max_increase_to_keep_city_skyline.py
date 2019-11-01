# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxi = [max(x) for x in grid]
        maxj = []
        for i in range(len(grid)):
            jarray = []
            for j in range(len(grid)):
                jarray.append(grid[j][i])
            maxj.append(max(jarray))
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                res += min(maxi[i], maxj[j]) - grid[i][j]
        return res
