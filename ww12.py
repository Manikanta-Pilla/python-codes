def fun(a):
    if(a<0):
        return 0
    print(a)
    fun(a-2)
    if(a!=1 and a%2!=0):
        print(a)

fun(5)
