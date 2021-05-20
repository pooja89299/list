 
# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ] 
# for line in open('magic square Input.txt'):
#     square=[int(n) for n in line.split()]
#     if len (set(square)) != len (square):
#         print("Invalid:duplicates")
#     else:
#         for idx in indexes:
#             if sum(square[i] for i in idx) !=15:
#                 print('Invalid:sum')
#                 break
#         else:
#             print("valid")




# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ] 
# i=0
# s=0
# while i<len(magic_square):
#     col=0
#     while col<len(magic_square):
#         s=s+magic_square[i][col]
#         col=col+1
#         # break
#     i=i+1
# print(s)
# x=0
# s1=0
# while x<len(magic_square):
#     row=0
#     while row<len(magic_square):
#         s1=s1+magic_square[x][row]
#         row=row+1
#         break
#     x=x+1
# print(s1)
# k=0
# s2=0
# while k<len(magic_square):
#     dig=0
#     while  dig<len(magic_square):
#         if k==dig:
#             s2=s2+magic_square[k][dig]
#         dig=dig+1
#     k=k+1
# print(s2)
# if s==s1==s2:
#     print("it is magic square")
# else:
#     print("it is not magic square")






# # s = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# # l = s.split()
# # k = []
# for i in l:
#     if (s.count(i)>1 and (i not in k)or s.count(i)==1):
#         k.append(i)
# print(' '.join(k))





# while i<len(l):
#     if l[i]=="over":
#         continue
#     print(l[i])
#     i+=1







# a =[12,32]
# for i in range(a):
#     print(a[i])
#  12 
#  10 // digit nikalo 
#  2
#  ""



# a=[12,42,70304]
# i=0
# while i<len(a):
#     i=i+1
# print(a)
# num = int(input("Enter"))
# result = []
# for index, digit in enumerate(str(num)[::-1]):
#     if int(digit) != 0:
#         result.append(digit + ('0' * index))
# print(result)

# A = [7000, 400, 70,1]
# cond = True
# y = 0
# i = 0
# sizeArray = len(A)
# for i in range(0, sizeArray-1):
#     while cond == True:
#         if A[i]%10 == 0:
#             A[i] = A[i]/10
#             y += 1

#         else:
#             cond = False
#     print(y)

def expanded_form(num):
    a =[]
    number = num
    while number != 0:
        number, rem = divmod(number, 10)
        a.append(rem)
    a.reverse()

    b = []
    counter = len(a)
    for n in a:
        b.append(n*(10**(counter-1)))
        counter-=1


    return ' + '.join([str(num) for num in b if num != 0])

    num = [34,45,8909]
    