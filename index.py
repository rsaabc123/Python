# sets: collectors of unique items

import time

'''
numbers = {1, 2, 2, 3}
print(numbers) # output: {1, 2, 3}, only store unique values
'''

attendance_logs1 = ['Alice', 'Bryan', 'Cathy', 'Cathy', 'Cathy', 'Dugan'] # list

attendance_logs2 = {'Alice', 'Bryan', 'Cathy', 'Cathy', 'Cathy', 'Dugan'} # set

start = time.perf_counter()
print(attendance_logs1)
time1 = time.perf_counter() - start

start = time.perf_counter()
print(attendance_logs2)
time2 = time.perf_counter() - start

print(f'list :{time1:.6f} seconds')
print(f'set :{time2:.6f} seconds')

# set has the ability to remove duplicates
# both collections list & set with duplicates, running printing set at majority of time cost less time than printing list