# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        one_step = head
        two_steps = head
        while two_steps and two_steps.next:
            one_step = one_step.next
            two_steps = two_steps.next.next
        return one_step
        
        
# Solution 2
#         count = 0
#         current = head
#         while current != None:
#             current = current.next
#             count +=1
        

#         steps = count // 2
#         current = head
#         while steps != 0:
#             current = current.next
#             steps -= 1
        
#         return current        
