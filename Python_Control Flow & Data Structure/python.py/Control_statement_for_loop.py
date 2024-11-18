'''
x={
    'TOC':77,
    'Python':90,
    'Computer Network':90,
    'Software Quality And Testing':85
}

for course,marks in x.items():
    print("{} : {}".format(course,marks))
'''

for x in range(10):
    if x==5:
        break
    print(x)
print()
for x1 in range(10):
    if x1==5:
        continue
    print(x1)