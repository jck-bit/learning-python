#global vs local variables
# global can be used everywhere

var = 9
loop = True

def func(x):
    newvar = 7
    print(loop)
    if x ==5:
        return newvar


func(2)