l=list(map(int,input().split()))
count=0
for i in l:
    if l[i]>l[i+1]:
        count+=1

print(count)
