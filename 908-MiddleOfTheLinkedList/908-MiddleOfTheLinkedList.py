# Last updated: 6/13/2025, 11:40:17 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # linked list counting method -> O(n)

        count = head
        length = 0

        while count:
            length += 1
            count = count.next
        
        for i in range(length // 2):
            head = head.next

        return head


        