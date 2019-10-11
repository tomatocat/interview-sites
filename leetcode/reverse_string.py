#https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n, i = len(s), 0
        while i < (n-1):
            e = s.pop()
            s.insert(i, e)
            i += 1
