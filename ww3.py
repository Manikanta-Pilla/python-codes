l1=list(input().split())
l2=[]
for i in l1:
    if(l1.count(i)%2!=0):
        l2.append(i)
print(l2)
