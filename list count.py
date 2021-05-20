s = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
l = s.split()
i=0
while i<len(l):
    if l[i]=="over":
        i+=1
        continue
    print(l[i],end=" ")
    i+=1