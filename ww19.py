def prime(n,i=2):
    if(n<=1):
        return False
    if n==2:
        return True
    if n%i==0:
        return False
        
    if i*i>n:
        return True
    return prime(n,i+1)

n=int(input())
res=prime(n)
if res==1:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")
