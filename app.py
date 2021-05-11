#functions in python

def addtwo(x):

    return x + 2


newnumber = addtwo(7)

print(newnumber)


def printstring(string):
    print(string)


printstring('hello world')

printstring('my name is jack')



def distance(speed, time):
    d = speed * time
    return d

print(distance(3,5))

def dosomething():
    print('am fine')
dosomething()