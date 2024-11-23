def first_even_number(numbers):
    for number in numbers:
        if number % 2==0:
            return number
    return None

result=first_even_number([1,4,3,2,5,6,7,8,9,10])
print(result)