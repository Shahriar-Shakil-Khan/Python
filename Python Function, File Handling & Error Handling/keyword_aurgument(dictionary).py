def dic(**person):
    for key, value in person.items():
        print(key+" : "+str(value))

dic(
      name='Shakil Khan',
      age='24',
      university='AIUB',
    city='Mymensingh'

)

'''
def dic(**person):
    print(person)

dic(
      name='Shakil Khan',
      age='24',
      university='AIUB',
    city='Mymensingh'

)
'''