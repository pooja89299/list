# elements=[4,3,6,7,126,7,13,23,12,15]
# i=0
# l=elements[0]
# while i<len(elements):
#     if elements[i]>l:
#           l=elements[i]
#     if elements[i]<l: 
#         f=elements[i]           
#     i=i+1    
# print(l,"largest")
# print(f,"smallest")






# e=[4,43,6,7,126,7,13,23,12,15]
# i=0
# c=e[0]
# while i<len(e):
#     if e[i]>c:
#         c=e[i]
#     if e[i]<c:
#         f=e[i]
#     i=i+1
# print(c,"grater")
# print(f,"smaller")





# num=[23,56,78,12,32,55,20]
# i=0
# b=num[1]
# while i>len(num):
#     if num[i]>b:
#         b=num[i]
#     i=i+1
# print("greaters",b)




num=[23,56,78,12,32,75,55,20]
i=1
var=num[0]
a=[]
while i<len(num):
    num1=num[i]
    if num1>var:
        var=num1
    i=i+1
num.remove(var)
y=0
var2=num[0]
s=[]
while y<len(num):
    n=num[y]
    if n>var2:
        var2=n
    y=y+1
a.append(var2)
print(a)

