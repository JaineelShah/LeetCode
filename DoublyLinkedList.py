class Node:
 	
		def __init__(self,data):
			self.prev=None
			self.next=None
			self.data=data

class DoublyLinkedList:

		def __init__(self):
			self.head=None

		def insertatbegin(self,data):
				new_node=Node(data)
				new_node.next=self.head
				if self.head is not None:
					self.head.prev=new_node
				self.head=new_node

		def insertatend(self,data):
				if self.head is not None:
						curr=self.head
						while curr.next is not None:
							curr=curr.next
						new_node=Node(data)
						curr.next=new_node
						new_node.prev=curr

				else:		
						new_node=Node(data)
						self.head=new_node
						print(self.head)
			
		def deletebegin(self):
				curr=self.head
				self.head=curr.next
				curr.next.prev=None
				curr.next=None

		def deleteend(self):
				curr=self.head

				while curr.next.next is not None:
					curr=curr.next
				curr.next.prev=None
				curr.next=None	
				
		def deleteatk(self,k):
				curr=self.head
				i=0

				while i<k-1:
					curr=curr.next
					i+=1
				curr.next.prev=curr.prev
				curr.prev.next=curr.next

		def deletek(self,k):

				curr=self.head

				while curr.data!=k:
					curr=curr.next
					
				curr.next.prev=curr.prev
				curr.prev.next=curr.next

		def reverselist(self):
			curr=self.head

			while curr:
				temp=curr.prev
				curr.prev=curr.next
				curr.next=temp
				curr=curr.prev

			self.head=temp.prev


		def display(self):
				curr=self.head
				a=[]
				while curr is not None:
					a.append(curr.data)
					curr=curr.next
				print(a)


obj=DoublyLinkedList()
# n1=Node(1)
# obj.head=n1
# obj.insertatbegin(2)
# obj.insertatbegin(3)	
# obj.insertatbegin(4)			

obj.insertatend(1)
obj.insertatend(2)
obj.insertatend(3)
obj.insertatend(4)
obj.display()
# obj.deletebegin()
# obj.deleteend()
# obj.deletek(2)
obj.reverselist()

obj.display()

	 		

		

	
