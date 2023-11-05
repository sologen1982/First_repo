text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# words_1 = text.split()    # разбить строку на слова и получить список слов или как ниже
# print(words_1)


words = []
start = 0
for indx, char in enumerate(text):
    if not char.lower() in alphabet:
        word = text[start:indx]
        words.append(word.strip())
        start = indx
print(words)


