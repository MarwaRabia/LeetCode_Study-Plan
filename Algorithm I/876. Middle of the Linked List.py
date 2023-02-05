"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.


Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      #two pointers technique with slow runner and fast runner.
      #Both slow runner and fast runner are initialized to head node.
      #Each iteration, fast runner moves two steps forward while the slow one moves one steps only.
      #When fast runner meets the empty node (i.e., NULL) on the tail, the slow one will be right on the node of midpoint.
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow
