age = input('What is your age? ')
age = int(age)

'''
if age >=18:
    print('Your age is {}.'.format(age))
    print('Adult')
elif age >=6:
    print('Your age is {}.'.format(age))
    print('Teenager')
else:
    print('Kid!')
'''

if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')