#create node_declaration &definition
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlelinkedlist:
    def _init_(self):
        self.head=None
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,end=" ")
                #temp.data means first node's data
                if temp.next!=None:
                    print("->",end=" ")#used to remove"->" at last
                temp=temp.next#establishing link
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_end(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
    def delete_position(self,pos):
        temp=self.head.next
        prev=self.head
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.next=None
obj=Singlelinkedlist()
#Node creation-initialisation
n=Node(10)#so n.data in node class will be 10
obj.head=n   #assigning first node as head 
n1=Node(20)
obj.head.next=n1  #next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print("\nafter deleting at begin")
obj.delete_begin()
obj.display()
print("\nafter deleting at end")
obj.delete_end()
obj.display()
print("\nafter deleting at pos")
obj.delete_position(2)
obj.display()