"""
for i in range(1, 10):
    print(i) # 2nd num excluded

for i in range(2, 257, 2):
    print(i) # step/increment: 2

for char in 'Python':
    print(char) # iterate over the string 'Python'"""

# Countdown - 10s

import time # built-in module

for i in range(10, 0, -1):
    print(i)
    time.sleep(1) # sleep for 1s before execute next task
print(0)
print('Times up!')