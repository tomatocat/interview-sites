# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict = {}
        for x in nums:
            dict[x] = 1
        arr = []
        for x in range(len(nums)):
            if (x+1) not in dict:
                arr.append(x+1)
        return arr
