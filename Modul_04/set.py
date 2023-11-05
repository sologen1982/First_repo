text = 'Lorem Ipsum \
    is simply dummy text of the printing and typesetting industry. \
        16522 . & gergerg   %#$^%&**'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

char_set = set()
symbol_set = set()

for el in text:
    if el.lower() in alphabet:
        char_set.add(el)
    else:
        symbol_set.add(el)

print(f'Chars {char_set}')
print(f'Symbols {symbol_set}')