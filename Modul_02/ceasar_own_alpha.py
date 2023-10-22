clean_text = "cowwr arhwb"
alphabet = "abhelcowdr"

shift = -3

encoded_text = ""

for i in clean_text:
    if i.isalpha():
        idx = alphabet.index(i)

        encoded_idx = (idx + shift) % len(alphabet)

        encoded_text += alphabet[encoded_idx]
    else:
        encoded_text += i

print(encoded_text)
