#implementation of single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
    def insertatbegin(self):
        n=Node(300)
        temp=self.head
        temp.prev=n
        n.next=temp
        self.head=n
    def insertatend(self):
        n=Node(400)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=n
        n.prev=temp
    def insertatpos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n
    def deleteatbegin(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def deleteatend(self):
        temp=self.head.next
        prev=self.head
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def deleteatpos(self,pos):
         temp=self.head.next
         prev=self.head
         for i in range(1,pos-1):
                temp=temp.next
                prev=prev.next
         prev.next=temp.next
         temp.next=prev.next
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                print(temp.data,end=" ")
                if temp.next!=None:
                    print("<-->",end=" ")
                temp=temp.next
    def reverse(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            while temp:
                     print(temp.data,end=" ")
                     if temp.prev!=None:
                      print("<-->",end=" ")
                     temp=temp.prev
obj=dll()
n1=Node(1)
obj.head=n1
n2=Node(2)
obj.head.next=n2
n2.prev=n1
n3=Node(3)
n2.next=n3
n3.prev=n2
obj.display()
print("\nafter inserting at first")
obj.insertatbegin()
obj.display()
print("\ninserting at end")
obj.insertatend()
obj.display()
print("\ninserting at position")
obj.insertatpos(3)
obj.display()
print("\nreverse order")
obj.reverse()
print("\ndeleting at begin")
obj.deleteatbegin()
obj.display()
print("\ndeleting at end")
obj.deleteatend()
obj.display()
print("\ndeleting at position")
obj.deleteatpos(3)
obj.display()