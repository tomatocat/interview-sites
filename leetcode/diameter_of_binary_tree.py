# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        #[maxDiameter, height]
        if not root:
            return [0, 0]
        l = self.helper(root.left)
        r = self.helper(root.right)
        maxl = l[0]
        maxr = r[0]
        maxtotal = (1 + l[1] + r[1])
        height =  1 + max(l[1], r[1])
        return [max(maxl, maxr, maxtotal), height]
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        x = self.helper(root)
        return x[0] - 1
        
