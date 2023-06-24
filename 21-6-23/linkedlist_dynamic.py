class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlelinkedlist:
    def _init_(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=None(data)
            self.last_node=self.head
        else:
            self.last_node.next=Node(data)
            self.last_node=self.last_node.next
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end="")
            current=current.next
a_llist=Singlelinkedlist()
n=int(input("how many elements/n"))
for i in range(n):
    data=int(input('enter data items:'))
    a_llist.append(data)
print('the linked list:',end='')
a_llist.display()