def fun(n):
    if n==0:
        return 0
    fun(n-1)
    print(n)

x=int(input("enter no:"))
fun(x)
