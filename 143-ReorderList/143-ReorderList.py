# Last updated: 6/13/2025, 11:40:27 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # half and reverse method -> O(n) time and O(1) space
        
        # find half
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next
        
        middle = length // 2

        new_curr = head

        for i in range(middle):
            new_curr = new_curr.next
        
        new_head = new_curr

        # reverse the remaining list 
        prev = None
        curr = new_head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # alternatively merge
        second_half = prev
        first_half = head

        while second_half and second_half.next:
            temp1 = first_half.next
            temp2 = second_half.next

            first_half.next = second_half
            second_half.next = temp1

            first_half = temp1
            second_half = temp2