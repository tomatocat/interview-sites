# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, sum, started):
        if not root:
            return 0
        if started:
            if root.val == sum:
                return 1 + self.helper(root.left, sum - root.val, True) + self.helper(root.right, sum - root.val, True)
            else:
                return self.helper(root.left, sum - root.val, True) + self.helper(root.right, sum - root.val, True)
        else:
            return self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
            
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.helper(root, sum, True) + self.helper(root, sum, False)
        
