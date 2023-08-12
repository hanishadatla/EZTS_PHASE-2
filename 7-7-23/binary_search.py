a=[1,2,3,4,5]
se=int(input("enter search elements"))
l=0
h=len(a)-1
f=0
while l<=h:
    mid=(l+h)//2
    if se==a[mid]:
        print("ele found at pos",mid)
        f+=1
        break
    elif se<a[mid]:
        h=mid-1
    elif se>a[mid]:
        l=mid+1
if f==0:
    print("not found")