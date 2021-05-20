
# 3 reverse

# num=int(input("enter a number"))
# rev=0
# while num>0:
#     rev=(rev*10)+num%10
#     num=num//10
# print("reverse num=",rev//10*10)





# 4 make the pattem


# n=int(input("enter a number"))
# i=1
# while i<=n:
#     j=1
#     while j<=5-i:
#         print(" ",end= " ")
#         j=j+1
#     k=1
#     while k<i:
#         print(k, end= " ")
#         k=k+1
#     b=i
#     while b>0:
#         print(b ,end=  " ")
#         b=b-1
#     print()
#     i=i+1


# 8 fizz

# y=1
# while y<50:
#     # n=int(input("enter a number"))
#     if y%3==0 and y%5==0:
#         print("fizz buzz")
#     if y%3==0:
#         print("fizz")
#     elif y%5==0:
#         print("buzz")
#     else:
#         print(y)
#     y=y+1
# print()


# 5 pattrn

# i=7
# while i>=1:
#     l=6
#     while l>=i:
#         print("",end=" ")
#         l=l-1
# # print()
#     j=1
#     while j<=i:
#         if j%2==0:
#             print("0",end="")
#         else:
#             print("1",end=" ")
#         j=j+1
#     i=i-2
#     print()
#   



# 5 pattern the

# row=int(input("enter a number:row"))
# colum=int(input("enter a colum"))
# i=1
# while i<=row:
#     j=1
#     while j<=colum:
#         if i%2 != 0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         j+=1
#     i=i+1
#     print()



# 9 num perform

# num=int(input("enter a number"))
# i=0
# while i<1:
#     if num%2==0 and num>=2 and num<=5:
#         print("NOT weird")
#     elif num%2==0 and num>=6 and num<=20:
#         print("weirrd")
#     elif num%2==0 and num>=20:
#         print("not weird")
#     else:
#         print("weird")
#     i=i+1

# 4 AsCll

# i=1
# a=65
# while i<=97:
#     print(chr(a),"=",a)
#     a=a+1
#     print()
#     i=i+1

# 6 series

# n=int(input("enter a number"))
# i=0
# count=int(input("enter a count"))
# sum=0
# while i<count:
#     a=n*(10**i)
#     sum=sum+a
#     print(a,"",end="")
#     i=i+1
# print(" series:",sum)

# 2 num

# n=int(input("enter a number"))
# i=0
# while i<1:
#     print((n*n)+(n-1)*(n-1))
#     i=i+1


# list=["swti","muskan","priyanka","madu"]
# print(list[2])


# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# a=[]
# i=1
# while i <len(binary_number):
#     print(binary_number)
#     i=i+1



# numbers=[50,40,23,70,56,12,5,10,7]
# i=0
# max=0
# while i<len(numbers):
#     if numbers[i]>max:
#         max=numbers[i]
#     i=i+1
# print(max)



# a=['n','i','t','i','n']
# b=[]
# length=len(a)
# print(length)
# i=1
# while i<=len(a):
#     b.append(a[-i])
#     i=i+1
# print(a)
# print(b)
# if b==a:
#     print("this is a palindrome")
# else:
#     print("not palindrome")




# # binary_number=int(input("enter a number"))
# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# i=1
# # b=[]
# content=0
# while i<=len(binary_number):
#     content=content+2**2*i-0*binary_number[-i]
#     i=i+1
# print(content)
# print(i)


# binary_number = [1,0,0,1]
# i=0
# sum=0
# l=len(binary_number)
# while i<len(binary_number):
#     num=binary_number[l-i-1]
#     sum=sum+num*(2**i)
#     print(i)
#     i=i+1
# print(sum)












