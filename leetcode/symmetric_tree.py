# https://leetcode.com/problems/symmetric-tree/

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.help(root.left, root.right)
    
    def help(self, l, r):
        if l == None or r == None:
            return l == None and r == None
        return l.val == r.val and self.help(l.left, r.right) and self.help(l.right, r.left)
