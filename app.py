#classes and objects in python 
# a method applies an object to itself
#a function takes an ob ject and aplies an operation to it




class dog(object):
    def __init__(self ,name, age):
        self.name = name
        self.age = age
        print('nice you made a scarf')

    def speak(self):
        print('hi am', self.name,'and am' ,self.age, 'years old')


"""the speak method automatically takes self"""
jack = dog('jack' , 19)
fred = dog('fred' ,5)
jack.speak()
fred.speak()

print(jack.age)