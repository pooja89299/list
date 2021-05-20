char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
y=[]
i=0
while i<len(char_list):
    j=0
    count=0
    l=[]
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    l.append(char_list[i])
    l.append(count)
    if l not in y:
        y.append(l)
    i=i+1
print(y)