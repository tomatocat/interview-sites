# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Already done last year with a flag. This time without a flag.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ''' recursive solution
        if not root:
            return []
        res = []
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res
        '''
        # iterative solution
        if not root:
            return []
        res, stack = [], []
        ptr = root
        stack.append(ptr)
        # get the leftmost node, keep a stack of nodes traveled through
        while ptr.left:
            ptr = ptr.left
            stack.append(ptr)
        while stack:
            ptr = stack.pop()
            res.append(ptr.val)
            if ptr.right:
                ptr = ptr.right
                stack.append(ptr)
                while ptr.left:
                    ptr = ptr.left
                    stack.append(ptr)
        return res
