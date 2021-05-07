#chained conditionals and nested statements
x = 2
y = 3

if not(y ==x or x + y==5):
    print('come')
else:
    print(':(')

x = 2
y = 3

if x ==2:
    if y ==3:
        print('x = 2, y=3')
    else:
        print('x= 2, y != 3')
else:
    print('x ! =2')