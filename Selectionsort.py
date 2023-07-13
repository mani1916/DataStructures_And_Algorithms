a=[4,2,56,3,1,4,56,2,2,7,3,2,3]
c=0
for i in range (len(a)):
    minIndex=i
    for j in range (i+1,len(a)):
        if a[j]<a[minIndex]:
            minIndex=j
    if(i!=minIndex):
        temp=a[i]
        a[i]=a[minIndex]
        a[minIndex]=temp

print(a)