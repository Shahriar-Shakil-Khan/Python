x={1,2,3,4,5}
first_location=id(x)
print(x)
print(type(x))
print(first_location)
x.add(6)
second_location=id(x)
print(x)
print(type(x))
print(second_location)


