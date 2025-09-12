import random

def get_user_guess():
    while True:
        try:
            return int(input('Insert an integer'))
        except ValueError:
            print('Invalid input')

def check_guess(secret, guess):
    if guess == secret:
        print(f'Bingo! Secret: {secret}')
    elif abs(secret - guess) <= 5:
        print('Hot')
    else: 
        print('Cold')
    return False 
    

def main():
    secret_number = random.randint(1, 10)
    MAX_TRIES = 5
    tries = 0

    while tries < MAX_TRIES:
        guess = get_user_guess()

        if check_guess(secret_number, guess):
            break
        tries += 1

    if tries == MAX_TRIES:
        print('Out of tries')

if __name__ == '__main__':
    main()