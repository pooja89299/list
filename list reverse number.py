i=0
a=[]
while i<10:
    n=int(input("Enter the number"))
    a.append(n)
    i=i+1
p=len(a)-1  
k=[]
while p>=0:
    k.append(a[p])
    p=p-1
print(a)
print(k)   