# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        val = postorder.pop() 
        i = inorder.index(val)
        inorderL, inorderR = inorder[:i], inorder[i+1:]
        size = len(inorderL)
        postorderL, postorderR = postorder[:size], postorder[size:]
        left = self.buildTree(inorderL, postorderL)
        right = self.buildTree(inorderR, postorderR)
        return TreeNode(val, left, right)
