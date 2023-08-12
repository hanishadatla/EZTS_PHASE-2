a=[1,2,3,4]
n=int(input("enter element"))
c=0
for i in range(len(a)):
    if a[i]==n:
        print("element found at",i)
        c+=1
        break
if c==0:
    print("not found")