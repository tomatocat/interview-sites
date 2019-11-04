# https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        curr, left, n = 1, [], len(nums)
        for j in range(n):
            left.append(curr)
            curr *= nums[j]
        i, curr, right = n-1, 1, [1]*n
        while i >= 0:
            right[i] = curr
            curr *= nums[i]
            i -= 1
        for j in range(n):
            left[j] *= right[j]
        return left
        
