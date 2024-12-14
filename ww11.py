def fun(a):
    if a==0:
        return 0
    if a%2!=0:
        print(a)
    fun(a-1)
    if a!=1 and a%2!=0:
        print(a)

    
        
        
        
x=int(input("enter no:"))
fun(x)
