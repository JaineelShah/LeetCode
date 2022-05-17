class Node:
    def __init__(self,data): 
        self.data=data
        self.next=None
        
class LinkedList:
    
    def __init__(self):
        self.head=None
    
    def appendlist(self,data):
        new_node=Node(data)
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node

    def appendbeginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def appendatk(self,data,k):
        new_node=Node(data)
        i=1
        curr=self.head
        while i<k:
          curr=curr.next
          i+=1
        new_node.next=curr.next
        curr.next=new_node
  
    def display(self):
        curr=self.head
        a=[]
        while curr is not None:
            a.append(curr.data)
            curr=curr.next
        print(a)

    def deletefirst(self):
        curr=self.head
        curr=curr.next
        self.head=curr

    def deletelast(self):
        curr=self.head
        while curr.next.next!=None:
          curr=curr.next
        curr.next=None
    
    def deleteany(self,a):
        curr=self.head
        if curr.data==a:
          curr=curr.next
          self.head=curr
        else:
          while curr.next.data!=a:
            curr=curr.next
          curr.next=curr.next.next

    def reverselist(self):

        curr,prev=self.head,None
        
        while curr is not None:
          temp=curr.next
          curr.next=prev
          prev=curr
          curr=temp
        self.head=prev



        
    
obj=LinkedList()

# obj.appendlist(5)
obj.appendbeginning(1)
obj.appendbeginning(5)
obj.appendbeginning(4)
obj.appendbeginning(6)
obj.display()
obj.reverselist()
obj.display()

# obj.deleteany(5)
# obj.appendatk(6,2)
# obj.deletefirst()
# obj.display()
              
