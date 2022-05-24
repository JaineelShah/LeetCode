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
        #M-1
        # a=[]
        # curr=head
        # while curr:
        #     a.append(curr)
        #     curr=curr.next
        # return(a[len(a)/2])
        
        #M-2 Fast and slow pointers
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
            
        
    
            
