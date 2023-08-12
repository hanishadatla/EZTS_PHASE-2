arr=[99,3,6,22,4,1]
for i in range(len(arr)):
    min=i#initial value
    for j in range(i+1,len(arr)):
        if arr[min]>arr[j]:
            min=j#finding min element index     
    #swapping element with min value
    arr[i],arr[min]=arr[min],arr[i]
print(arr)