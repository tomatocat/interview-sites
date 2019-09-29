# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        tmp = head.next
        head.next = None
        while tmp:
            tmp2 = tmp.next
            tmp.next = head
            head, tmp = tmp, tmp2
        return head
