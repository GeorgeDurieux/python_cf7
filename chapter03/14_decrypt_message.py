def decrypt_message(message):
    decrypted_message = ''
    for char in message:
        if not char.isnumeric():
            decrypted_message += char

    return decrypted_message

def main():
    strange_message = '298H123e314l3678l8423o25 524C642F2466'

    decrypted_message = decrypt_message(strange_message)
    
    print(decrypted_message)

if __name__ == '__main__':
    main()