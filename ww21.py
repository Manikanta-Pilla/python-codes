def rev(n,re=0):
    if(n==0):
        return re
    else:
        d=n%10
        re=re*10+d
        return rev(n//10,re)
    if n==rev:
        return n
n=int(input())
res=rev(n)
if res==n:
    print(f"{n} is palindromr")
else:
    print(f"{n} is not palindrome")
