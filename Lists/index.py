# list: ordered collection/used to store sth

list_fruits = ['apple', 'banana', 'orange', 'watermelon']

list_colors = ['red', 'yellow', 'blue', 'green', 'purple']

list_occupations = ['lawyer', 'police officer', 'doctor', 'engineer', 'HOA']

print(list_fruits) # print list_fruits

print(list_fruits[0]) # access item in list_fruits at index 0 ('apple')

print(list_fruits + list_colors) # combining two lists

list_fruits[0] = 'peach'; print(list_fruits) # replacing item in list_fruits at index 0 to 'peach'

list_colors.append('gray'); print(list_colors) # appending a new color (color 'gray') in list_colors (append adds the item to the last position in the list)

list_occupations.pop(-1); print(list_occupations) # pop (to remove) an item from the list based on the index position
