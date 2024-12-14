def fun(a):
    if(a==1):
        return 0
    return a+fun(a-1)

x=int(input())
print(fun(x))
