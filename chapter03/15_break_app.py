def main(): 
    months = ['Jan', 'Feb', 'Mar']

    input_month = input('3 letters:')

    found = False

    for month in months:
        if month.casefold() == input_month.casefold():
            found = True
            break
    
    print('Month found') if found else print('Not found')

    for month in months:
        if month.casefold() == input_month.casefold(): print('Found')
        break
    else:
        print('Not found')

if __name__ == '__main__':
    main()