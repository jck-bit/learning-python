##else statements

language = 'java'

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



a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)


#False values:
  #False
  #None
  #zero of any numeric type
  #an empty sequence .eg '', (), []
  #an empty mapping

condition = []

if condition:
    print('evaluated to true')
else:
    print('evaluated to False')
