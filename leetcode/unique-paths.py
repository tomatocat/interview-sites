# https://leetcode.com/problems/unique-paths/

class Solution(object):  

    def fact(self, n):
        if n == 0:
            return 1
        else:
            return n*self.fact(n-1)
    
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.fact(m+n-2)/((self.fact(m-1))*(self.fact(n-1)))        
