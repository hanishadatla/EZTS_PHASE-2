arr=[99,3,6,22,4,1]
for i in range(1,len(arr)):
    j=i
    while arr[j-1]>arr[j] and j>0:
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)