def merge(A,B):
    C= [0]*(len(A)+len(B))
    n1= len(A)
    n2=len(B)
    i=0
    j=0
    k=0
    while i<n1 and k<n2:
        if A[i]<B[j]:
            C[k]=A[i]
            k+=1
            i+=1 
        else:
            C[k]=B[j]
            k+=1
            j+=1 
    while i<n1:
        C[k]= A[i]
        k+=1
        i+=1 
    while j<n2:
        C[k]= B[j]
        k+=1
        j+=1 
    return C 
li=[1,2,3]
li1=[1,2,3,4]
print(merge(li,li1))