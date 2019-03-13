class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print current.data,
            current = current.next
    def insert(self,head,data): 
    #Complete this method
		if not head: #Check if ther are no nodes
			return Node(data)
		else:
			currentnode = head
			while currentnode.next != None: 
				currentnode = currentnode.next # move to next node
        		currentnode.next = Node(data) #next node points to the new node
        		return head
mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);	