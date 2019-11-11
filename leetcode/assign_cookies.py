# https://leetcode.com/problems/assign-cookies/

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s1, g1 = sorted(s), sorted(g)
        i, j = 0, 0
        while j < len(s1) and i < len(g1):
            if g1[i] > s1[j]:
                i -= 1
            i += 1
            j += 1
        return i
