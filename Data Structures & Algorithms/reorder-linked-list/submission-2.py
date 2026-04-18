class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head

        # Find the middle point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # Reverse second part
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev

        first = head
        while second:
            temp_1, temp_2 = first.next, second.next
            first.next = second
            second.next = temp_1
            first = temp_1
            second = temp_2
            
        return