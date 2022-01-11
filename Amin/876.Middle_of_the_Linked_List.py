#taken form solutions
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            # moves at speed V
            slow = slow.next
            # moves at speed 2V
            fast = fast.next.next
        return slow
