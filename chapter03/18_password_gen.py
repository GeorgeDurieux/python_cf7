import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*')

def generate_password():
    try:
        password_length = int(input('Length: '))

        if password_length <= 0: 
            print('Need positive')
            return
        
    except ValueError:
        print('Need integer')
        return
    
    random.shuffle(characters)

    password = []

    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = ''.join(password)

    return(password)

def main():
    while True:
        option = input('\nDo you want to create a password? "y/n": ')

        if option.lower() == 'y':
            print(generate_password())
        elif option.lower() == 'n':
            print('Ciao')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()