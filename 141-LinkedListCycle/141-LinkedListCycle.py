# Last updated: 6/13/2025, 11:40:28 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        visted = set()

        while head:
            if head in visted:
                return True
            else:
                visted.add(head)
                head = head.next
        
        return False
        