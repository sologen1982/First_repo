text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
dict_counter = {}     # {'L': 1, 'o':2}
for char in text:
    count = dict_counter.get(char, 0)
    count += 1 
    dict_counter[char] = count  #записуємо значення по ключу

print(dict_counter)