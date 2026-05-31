import random

while True:
    try:
        user_input = int(input("Enter Level: "))
        if user_input > 0:
            break
        else:
            raise ValueError

    except ValueError:
        continue


while True:
    try:
        user_guess = int(input("Guess: "))
        game = random.randrange(1, user_input)
        if user_guess <0:
            raise ValueError
        if user_guess == game:
            print("Just right!")
            break
        elif user_guess > game:
            print("Too large!")
            continue
        else:
            print("Too small!")
            continue
    except ValueError:
        continue
