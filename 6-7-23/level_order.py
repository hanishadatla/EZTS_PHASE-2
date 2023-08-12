class node:
    def _init_(self,key):
        self.left=None
        self.right=None
        self.val=key
def insert(root,key):
    if root is None:
        return node(key)
    else:
        if root.val==key:
            return root
        elif root.val <key:
            root.right=insert(root.right,key)
        else:
            root.left=insert(root.left,key)
    return root
def append(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
def inorder(root):
    if root:
            inorder(root.left)
            print(root.val,end=" ")
            inorder(root.right)
def level_order(root):
    queue=[root]
    while len(queue)!=0:
        ele=queue.pop(0)
        if ele.left!=None:
            queue.append(ele.right)
        if ele.right!=None:
            queue.append(ele.right)
        print(ele.val)
def search(root,key):
    if root is None or root.val ==key:
        return root
    if root.val <key:
        return search(root.right,key)
    return search(root.left,key)
n=int(input("how may elements would you like to add"))
for i in range(n):
    data=int(input("enter data items: "))
    if(i==0):
        r=node(data)
    else:
        insert(r,data) 
inorder(r)
n=int(input("\n enter search element"))
if search(r,n) is None:
    print("not found")
else:
    print("found")
