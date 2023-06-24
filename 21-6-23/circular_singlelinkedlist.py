class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlelinkedlist:
    def _init_(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_last(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
        ne.next=None
    def insert_pos(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):
            temp=temp.next
        np.next=temp.next
        temp.next=np
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
                temp.next=self.head 
obj=Singlelinkedlist()
#Node creation-initialisation
n=Node(10)#so n.data in node class will be 10
obj.head=n   #assigning first node as head 
n1=Node(20)
obj.head.next=n1  #next node value
n2=Node(30)
n1.next=n2
obj.display()
print("\nafter inserting at begin")
obj.insert_beginning(100)
obj.display()
print("\nafter inserting at end")
obj.insert_last(50)
obj.display() 
print("\n after inserting at pos")
obj.insert_pos(3,99)
obj.display()
