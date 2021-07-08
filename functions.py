
# keeping your code DRY..by avoiding repeating yourselves

#passing arguments in functions

def hell(greetings, name = 'you'):
    return '{}, {}'.format(greetings, name)

print(hell('hey'))


#args and kwargs

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('math', 'art', name = 'john', age = '23')

# args is positional  arguments while kwargs is a dictionary with all keywords values
