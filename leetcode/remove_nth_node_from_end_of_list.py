# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        d = []
        length = 0
        copy = head
        while head:
            d.append(head)
            head = head.next
        if len(d) == n:
            return copy.next
        prev = d[length - n - 1]
        prev.next = prev.next.next
        return copy
