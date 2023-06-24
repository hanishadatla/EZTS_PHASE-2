class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self,data):
        if self.last is None:
            self.head =node(data)
            self.last=self.head
        else:
            self.last.next=node(data)
            self.last=self.last.next
    def dequeue(self):
        if self.head is None:
            print("queue is empty")
        else:
            removed=self.head.data
            self.head=self.head.next
            print("the popped element is",removed)
            return removed
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("->",end=" ")
                temp=temp.next
obj=queue()
while True:
    print("\nselect operation 1.enqueue 2.dequeue 3.display 4.quit\n")
    ch=int(input())
    if ch==1:
        print("enter element to push")
        m=int(input())
        obj.enqueue(m)
    elif ch==2:
        obj.dequeue()
    elif ch==3:
        obj.display()
    elif ch==4:
        break
    else:
        print("invalid choice")