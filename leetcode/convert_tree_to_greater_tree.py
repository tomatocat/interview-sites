# a modified version of
# https://leetcode.com/problems/convert-bst-to-greater-tree/
# where we don't assume the tree is a BST

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = self.help(root)
        arr.sort(reverse = True)
        return self.add(root, arr)
    
    def add(self, t, arr):
        if not t or len(arr) < 1:
            return None
        x, i = t.val, 0
        while x < arr[i] and i < len(arr):
            t.val += arr[i]
            i += 1
        t.left = self.add(t.left, arr)
        t.right = self.add(t.right, arr)
        return t
        
    def help(self, root):
        if not root:
            return []
        return [root.val] + self.help(root.left) + self.help(root.right)
