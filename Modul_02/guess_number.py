import random

tries = -1
number = random.randint(0, 100)

while True:
    tries += 1

    if tries > 7:
        raise RuntimeError("You looser!")
    
    guess = input("I thought a number what is it?: ")

    if guess == "exit":
        print("bye, bye")
        break

    if not guess.isnumeric():
        print(f"Bad number '{guess} !")

    int_guess = int(guess)

    if not 0 <= int_guess <= 100:
        print(f"Bad number '{guess} !")
        continue

    if int_guess > number:
        print("Too Big!")
    elif int_guess < number:
        print("Too Low!")
    else:
        print("You guessed! Win! Great!")
        break

