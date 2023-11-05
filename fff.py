import random

def get_random_password():
    password = ""
    for _ in range(8):
        random_num = random.randint(40, 126)
        password += chr(random_num)
    return password

