name = input('Insert your name: ')
age = int(input('Insert your age: '))
height = float(input('Please enter your height: '))
is_student = (input('Are you a student? (Yes/No): ')).lower() == 'yes'

print(f'Hello {name}!')

if is_student:
    print('You are a student')
else:
    print('You are not a student') 

print('Your age is {} and your height is {:.2f}'.format(age, height))
