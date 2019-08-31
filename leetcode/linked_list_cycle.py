# https://leetcode.com/problems/linked-list-cycle/

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        p1 = head.next
        p2 = head.next.next
        while p1 and p2 and p2.next:
            if p1 is p2:
                return True
            p1 = p1.next
            p2 = p2.next.next
        return False
