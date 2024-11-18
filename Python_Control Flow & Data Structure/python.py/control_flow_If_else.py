'''
age=int(input("Enter your age : = "))

if age>=18:
    print("You are not child")
else:
    print("you are child")


a=int(input("Enter a : = "))
b=int(input("Enter b : = "))

if a>b:
    print(" a is greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater than a")

'''

#nested if and else
age=int(input("Enter your age : = "))
has_permission=False

if age>=18:
    if has_permission==True:
        print("You are enter the club")
    else:
        print("You need the permission to enter the club")
else:
    print("You are not allowed not enter the club")



