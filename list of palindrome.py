a=['n','i','t','i','n']
b=[]
# length=len(a)
# print(length)
i=1
while i<=len(a):
    b.append(a[-i])
    i=i+1
# print(a)
# print(b)
if b==a:
    print("this is a palindrome")
else:
    print("not palindrome")