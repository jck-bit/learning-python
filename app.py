#try and except (try & accept)
text = input('username: ')

try:
    number = int(text)
    print(number)

except:
    print('invalid username')

