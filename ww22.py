def arm(n,rev=0):
    if(n==0):
        return rev
    else:
        d=n%10
        rev=rev+d**s
        return arm(n//10,rev)
n=int(input())
st=str(n)
s=len(st)
res=(arm(n))
if res==n:
    print(f"{n} is armstrong")
else:
    print(f"{n} is not armstrong")
