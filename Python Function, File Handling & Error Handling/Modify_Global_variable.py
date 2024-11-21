x = 10


def sum1():
    global x
    x=50
    res=x+1
    print("Local : ",res)


def sum2():
    res = x + 2
    print("Local : ",res)

sum1()
sum2()