# https://leetcode.com/problems/counting-bits/

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        i = 1
        nextpow = 1
        j = 0
        res = [0]
        while i <= num:          
            if i == nextpow:
                res.append(1)
                j = 0
                nextpow *= 2
            else:
                res.append(1+res[j])
            j += 1
            i += 1
        return res
