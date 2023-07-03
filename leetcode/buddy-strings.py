# https://leetcode.com/problems/buddy-strings/
# Time: O(n)
# Space: O(n)

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        # must be same length
        if len(s) != len(goal):
            return False

        # swap 2 same chars
        charset, repeatchar = set(), False
        for i in range(0, len(s)):
            if s[i] in charset:
                repeatchar = True
                break
            charset.add(s[i])
        if s == goal and repeatchar:
            return True
        
        # swap 2 different chars
        different, a, b = [], [], []
        for i in range(0, len(s)):
            if s[i] != goal[i]:
                different.append(i)
                a.append(s[i])
                b.append(goal[i])
        if len(different) == 2 and a[0] == b[1] and a[1] == b[0]:
            return True        
        
        # not found
        return False
