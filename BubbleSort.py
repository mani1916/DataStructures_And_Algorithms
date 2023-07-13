a=[4,2,56,3,1,4,56,2,2,7,3,2,3]

for i in range (1,len(a)):
    for j in range (0,len(a)-1):
        if(a[j]<a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print(a)
