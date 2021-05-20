binary_num=[1,1,1]
i=0
sum=0
l=len(binary_num)
while i<len(binary_num):
    num1=binary_num[l-i-1]
    sum=sum+num1*(2**i)
    i=i+1
print(sum)