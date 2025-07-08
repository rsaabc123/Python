# tuples: immutable order (fixed data)

# tuples are used for data protection from accidental changes

colors = ('red', 'yellow', 'blue', 'green')

try:
    colors[1] = 'orange'

except Exception as e:
    print(e)