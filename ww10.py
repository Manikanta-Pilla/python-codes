def fun(a):
    if a==0:
        print(0)
    else:
        print(a)
        fun(a-1)
        print(a)
        return 0

    
        
        
        
x=int(input("enter no:"))
fun(x)
