# https://leetcode.com/problems/palindromic-substrings/

class Solution(object):    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, res = len(s), 0
        #odds
        for i in range(n):
            j = 0
            while ((i-j)>=0) and ((i+j)<n):
                if s[i-j] == s[i+j]:
                    res += 1
                else:
                    break
                j += 1
        #evens
        for i in range(n):
            j = 0
            while ((i-j)>=0) and ((i+j+1)<n):
                if s[i-j] == s[i+j+1]:
                    res += 1
                else:
                    break
                j += 1
        return res
        
