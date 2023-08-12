def quick_sort(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    left=[i for i in a if i<pivot]
    right=[i for i in a if i>pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)

a=[1,5,3,6,2]
ans=quick_sort(a)
print(ans)
    