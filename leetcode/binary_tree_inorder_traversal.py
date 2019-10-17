# https://leetcode.com/problems/binary-tree-inorder-traversal/
# iterative solution

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [(root, 0)], []
        while stack:
            e = stack.pop()
            t = e[0]
            if t:
                if e[1] == 1:
                    res.append(t.val)
                else:
                    stack.append((t.right, 0))
                    stack.append((t, 1))
                    stack.append((t.left, 0))
        return res
