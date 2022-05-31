# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        slow=fast=head
        
        prev=None
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        while slow:
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        while prev:
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True
                
            


        
    
        
    
