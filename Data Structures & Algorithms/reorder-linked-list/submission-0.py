# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # Find the middle node of linked list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # Reverse list after middle node
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        first = head
        while second:
            temp_node1, temp_node2 = first.next, second.next
            first.next = second
            second.next = temp_node1
            first = temp_node1
            second = temp_node2