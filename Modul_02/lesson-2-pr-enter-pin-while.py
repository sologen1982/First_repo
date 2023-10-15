initial_pin = '0123'    # правильный пинн

n = 0                   # счетчик
max_tries = 3

while n < max_tries:

    user_pin = input('Enter your pin: ')

    if len(user_pin) == 4 or len(user_pin) == 6:

        if initial_pin == user_pin:
            
            amount = input('How much: ')

            if amount > 0:
            
                print(f'Take your {amount}')
                break

        else:
            print('Sorry, wrong pin. Try again please!')
            print(f'You have {max_tries - n - 1} tries.')
            n += 1
    
    else:
        print('Pin schould be 4 or 6 digits.')
    
    
print('Good bye')