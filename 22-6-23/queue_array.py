#stack implementation using arrays
stack=[]
def push():
    element=int(input("enter the element"))
    stack.append(element)
    print(stack)
def pop_element():
    if not stack:
        print("stack is empty")
    else:
        e=stack.pop(0)
        print("removed element:",e)
        print(stack)
def display():
    print("stack is:",stack)

while True:
    print("Select operation 1.push 2.pop 3.display  4.peek 5.quit")
    choice=int(input())
    if choice==1:
        push()
    elif choice==2:
        pop_element()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter the correct operation")
            
        