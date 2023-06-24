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
obj=Singlelinkedlist()
#Node creation-initialisation
n=Node(10)#so n.data in node class will be 10
obj.head=n   #assigning first node as head 
n1=Node(20)
obj.head.next=n1  #next node value
n2=Node(30)
n1.next=n2
obj.display()