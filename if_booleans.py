language = 'java'

##else statements



if language == 'python':
    print('the language is python')

elif language == 'java':
    print('the language is java')
else:
    print('no match')

##there are also
#and
#or
#not

User = 'Admin'
logged_in = False

if User == 'Admin' and logged_in:
    print('Admin page')
else:
    print('bad credentials')
