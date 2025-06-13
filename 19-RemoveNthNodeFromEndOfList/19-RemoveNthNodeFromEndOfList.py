# Last updated: 6/13/2025, 11:40:32 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # iterative method -> O(n) time

        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        index = length - n

        if index == 0:
            return head.next

        new_curr = head
        counter = 0

        while new_curr and new_curr.next:
            if counter == index - 1:
                new_curr.next = new_curr.next.next
                break
            else:
                counter += 1
                new_curr = new_curr.next
        
        return head

