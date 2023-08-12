arr=[99,3,6,22,4,1]
n=len(arr)
for i in range(n-1):
    swap=False
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            swap=True
            arr[j],arr[j+1]=arr[j+1],arr[j]
    if swap == False:
        break
print(arr)