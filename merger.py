def split(s,start,end):
    if(end -start==1):
        return s
    mid=len(s)//2
    split(s,start,mid)
    split(s,mid,end)

    return sort(a,start,mid,end)

def sort(s,start,mid,end):
    join=[]
    i=j=0
    while (start<mid and mid<end):
        if s[start]:
            join.append(start[i])
            i+=1;
        else:
            join.append()
            j+=1
    while (i<len(left)):
        join.append(left[i])
        i+=1
    while (j<len(right)):
        join.append(right[j])
        j+1

    return join


a=[9,8,7,6,5,4,3,2,1]
split(a,0,len(a))
print(a)