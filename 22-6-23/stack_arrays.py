#stack implementation using arrays
#implmentation of stack using arrays
stack=[]
def push():
    ele=int(input("enter the element"))
    stack.append(ele)
def pop_ele():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop()
        print("the removed element is:",e)
def display():
    print("stack is:",stack)
def peek():
    if not stack:
        print("stack is empty")
    else:
        print("the top element is :",stack[-1])
def seek():
    n=int(input("enter element to be searched"))
    c=0
    for i in range(len(stack)):
        if (n==stack[i]):
            c+=1
    if c>=1:
        print("found")
    else:
        print("not found")
while True:
    print("select operation 1.push 2.pop 3.display 4.peek 5.seek 6.quit\n")
    ch=int(input())
    if ch==1:
        push()
    elif ch==2:
        pop_ele()
    elif ch==3:
        display()
    elif ch==4:
        peek()
    elif ch==5:
        seek()
    else:
        print("select correct operation")