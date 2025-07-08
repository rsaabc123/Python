# functions: reusable block of code that performs a specific task

def greeting():
    print('Hello World')

# the statement 'Hello World' would not be performed unless called:

greeting()

#

def greet(name):
    print(f'Hello, {name}!')

greet('Bob') # passing 'Bob' to parameter name

def multiply(x, y):
    return x * y # return the product of 5 * 7

result = multiply(5, 7)
print(result)
