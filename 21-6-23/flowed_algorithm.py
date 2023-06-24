class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    #insert node at begining
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def detectAndRemoveLoop(self):
        if self.head is None:#linkeslist empty
            return
        if self.head.next is None:
            return
        slowp = self.head
        fastp = self.head
        
        while(slowp and fastp and fastp.next):
            slowp = slowp.next
            fastp = fastp.next.next
            
            #if slowp and fastp meet at some point
            #there is a loop
            if slowp == fastp:
                print("meeting point",slowp.data)
                slowp = self.head
                #finding the begining of the loop
                while (slowp.next != fastp.next):
                    slowp = slowp.next
                    fastp = fastp.next
                    #since fastp.next is the looping point
                print("start of loop",fastp.next.data)
                fastp.next = None #remove loop
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

llist = LinkedList()
llist.head = Node(50)
llist.head.next = Node(20)
llist.head.next.next = Node(15)
llist.head.next.next.next = Node(4)
llist.head.next.next.next.next = Node(10)
#create a loop for testiing
extra=Node(1)
llist.head.next.next.next.next.next=extra
extra.next=llist.head.next
#llist.printList()
llist.detectAndRemoveLoop()
print("Linked List after removing the loop")
llist.printList()