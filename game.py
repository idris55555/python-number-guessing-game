import random
from codecs import ignore_errors

low_num = 1
highest_num = 100
answer = random.randint(low_num,highest_num)
guesses = 0
is_running = True

print("python number guessing game !")
print(f"select a num between {low_num} and {highest_num}")

while is_running:
    guess = input("enter your guess :")

    if guess.isdigit():
        guess = int(guess)
        guesses +=1

        if guess > highest_num or guess < low_num:
            print(f"select a num between {low_num} and {highest_num} :")
        elif guess < answer:
            print("too low! try again :)")
        elif guess > answer:
            print("too ligh! try again :)")
        else:
            print(f"correct! the answer was {answer}")
            print(f"numbre of guesses is {guesses}")
            is_running = False
    else:
        print("invalid guess!")
        print(f"select a num between {low_num} and {highest_num} :")