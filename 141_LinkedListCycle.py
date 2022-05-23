# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        """
        :type head: ListNode
        :rtype: bool
       """
        
#     # M-1 Slow Fast Pointers
#         slow,fast=head,head
        
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#             if slow==fast:
#                 return True
#         return False
    
    #M-2 Using a Set
    
        curr=head
        setmap=set()
        
        while curr:
            if curr in setmap:
                return True
            else:
                setmap.add(curr)
                curr=curr.next
            
        return False
                
                
            
    
        
        
