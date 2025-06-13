# Last updated: 6/13/2025, 11:40:24 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # creating a "fake" head of linked list
        node = ListNode(None)
        node.next = head
        curr = node

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return node.next

        # O(n) time 

        

        