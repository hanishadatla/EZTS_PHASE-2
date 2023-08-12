def merge(a,left,mid,right):
    left_a=a[left:mid+1]
    right_a=a[mid+1:right+1]
    left_ind=0
    right_ind=0
    ind=left
    while left_ind <len(left_a)  and right_ind <len(right_a):
        if left_a[left_ind]<right_a[right_ind]:
            a[ind]=left_a[left_ind]
            left_ind+=1
        else:
            a[ind]=right_a[right_ind]
            righg_ind+=1
        ind+=1
    while right_ind <len(right_a):
        a[ind]=right_a[right_ind]
        right_ind+=1
        ind+=1
    while left_ind <len(left_a):
        a[ind]=left_a[left_ind]
        left_ind+=1
        ind+=1
    
def merge_sort(a,left,right):
    if left<=right:
        return
    mid=(left+right)//2
    merge_sort(a,left,mid)
    merge_sort(a,mid+1,right)
    merge(a,left,mid,right)
        
a=[5,3,67,55,2,1]
merge_sort(a,0,len(a)-1)
print(a)