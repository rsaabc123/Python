# dictionaries: key-value paired collections

person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'}

print(person['age'])
print(person.get('job', 'Not Specified')) # 'Not Specified' as default output if 'job' is not a key

'''
'''

#look up for one's information:

users = {
    'Alice': {'age': 25,
              'job': 'Designer'},
    'Bob':  {'age': 30,
              'job': 'Engineer'}}

print(users['Bob']['job'])