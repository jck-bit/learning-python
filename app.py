#iterating through a list.
#this is known as iterating by item
fruits = ['mango', 'apple', 'strawberry', 'banana']

for fruit in fruits:
    print(fruit)

#another example includes

for fruit in fruits:
    if fruit == 'banana':
        print('banana')
    else:
        print('not a banana')

#iterating using the indices method
for x in range(0, 3):
    if fruits[x] == 'banana':
        print(fruits[x])
    else:
        print('not a banana')
