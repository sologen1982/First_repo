while True:
    
    user_input = input("Enter number ")

    try:
        x = int(user_input)
    except ValueError:
        print('Value')
        continue
    except TypeError:
        print('Type')
        continue
    # else:
    #     print('Else')
    # finally:
    #     print('Finally')
    
    break

raise ValueError('Message')         # принудительный вызов исключений