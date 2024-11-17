'''
number=int(input("Please!enter any number as you wish : = "))
if number%2==0:
    print(number," is even number")
else:
    print(number," is odd number")
'''


number=int(input("Please!enter any number as you wish : = "))
if number%2==0 and number>=0:
    print(number," is even number and positive")
elif number%2==0 and number<0:
    print(number, " is even number and negative")
elif number % 2 == 1 and number >= 0:
    print(number, " is odd number and positive")
else:
    print(number, " is odd number and negative")


