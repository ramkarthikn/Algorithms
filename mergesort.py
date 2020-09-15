def mergesort(Arr):
    n=len(Arr)
    if n==1:
        return Arr
    mid= len(Arr)//2 
    b1= Arr[:mid]
    b2= Arr[mid:]
    mergesort(b1)
    mergesort(b2)
    i=0
    j=0
    k=0
    while i<len(b1) and j<len(b2):
        if b1[i]<b2[j]:
            Arr[k]=b1[i]
            k+=1
            i+=1 
        else:
            Arr[k]=b2[j]
            k+=1
            j+=1 
    while i<len(b1):
        Arr[k]=b1[i]
        k+=1
        i+=1
    while j<len(b2):
        Arr[k]=b2[j]
        k+=1
        j+=1 
    return Arr 
li=[1,2,3,112,2,12,24,124]
print(mergesort(li))