counter = 0
while counter < 5:
    user_input = input('>>> ')
    counter +=1     # counter = counter + 1
    if user_input == 'exit':
        break
    else:
        print(f'You write: {user_input}')