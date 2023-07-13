def split(s):
    if(len(s)==1):
        return s
    mid=len(s)//2
    left=split(s[:mid])
    right=split(s[mid:])

    return sort(left,right)

def sort(left,right):
    join=[]
    i=j=0
    while (i<len(left) and j<len(right)):
        if left[i]<right[j]:
            join.append(right[i])
            i+=1;
        else:
            join.append(right[j])
            j+=1
    while (i<len(left)):
        join.append(left[i])
        i+=1
    while (j<len(right)):
        join.append(right[j])
        j+1

    return join


a=[9,8,7,6,5,4,3,2,1]

print(split(a))