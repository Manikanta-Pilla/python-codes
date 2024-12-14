n=int(input())
result=0
flag=0
while(n):
    digit=n%10
    result=result+digit
    n=n//10
for i in range(2,(result//2)+1):
    if(result%i==0):
        flag=1
        break
if(flag==1):
    print("not googly")
else:
    print("googly")
    


