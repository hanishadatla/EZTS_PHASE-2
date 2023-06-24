#insert:rear=rear+1--we add new person at end
#delete:front+1--FIFO
class circularqueue():
    def _init_(self,size):
        #initialising the class
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        #condition if queue is full
        if ((self.rear+1)%self.size ==self.front):
            print("queue is full\n")
        #condition for empty queue
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #always add element at tail place
        else:
            #next position of rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if (self.front==-1):
            #condition for empty queue
            print("queue is empty\n")
        elif (self.front ==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        #condition for empty space
        if (self.front==-1):
            print("queue is empty\n")
        elif (self.rear >=self.front):
            print("elements in circular queue :",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("elements :",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end= " ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if ((self.rear+1)% self.size ==self.front):
            print("queue is full")
obj=circularqueue(5)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.display()
print("dequeued element is:",obj.dequeue())
print("dequeued element is:",obj.dequeue())
obj.display()
obj.enqueue(9)
obj.enqueue(99)
obj.enqueue(88)
obj.display()
obj.dequeue()
obj.enqueue(0)
obj.display()