#create node_declaration &definition
class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class Doublelinkedlist:
    def _init_(self):
        self.head=None
    def insert_start(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insert_end(self):
        n=Node(500)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insert_pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
        
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head #temp=first node
            while temp:
                print(temp.data,end=" ")
                #temp.data means first node's data
                if temp.next!=None:
                    print("<-->",end=" ")#used to remove"->" at last
                temp=temp.next#establishing link
obj=Doublelinkedlist()
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
n5=Node(60)
n4.next=n5
obj.display()
print("\nafter inserting at begin")
obj.insert_start()
obj.display()
print("\nafter inserting at end")
obj.insert_end()
obj.display()
print("\nafter inserting at pos")
obj.insert_pos(3)
obj.display()