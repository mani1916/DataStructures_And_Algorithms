def quicksort(a,low,high):
    if low>=high:
        return
    start=low
    end=high
    mid=(start+end)//2
    pivot=a[mid]
    while(start<=end):
        while(a[start]<pivot):
            start+=1
        while(a[end]>pivot):
            end-=1
        if(start<=end):
            temp=a[start]
            a[start]=a[end]
            a[end]=temp
            start+=1
            end-=1
    quicksort(a,low,end)
    quicksort(a,start,high)

n=[1,5,7,2,4,6]
quicksort(n,0,len(n)-1)
print(n)