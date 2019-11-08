# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        rest = self.permute(nums[1:])
        res = []
        item = nums[0]
        for x in rest:
            i = 0
            while i < len(nums):
                copy = x[:]
                copy.insert(i, item)
                res.append(copy)
                i +=1 
        return res
