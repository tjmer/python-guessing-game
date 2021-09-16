import random

player_name = input("Hello, what is your name: ")


def game_guess():
    comp_num = random.randint(1,100)
    guess_count = 0
    print("Guess a number between 1 and 100.")
    player_guess = float(input("What number did comp choose?: "))
    while player_guess != comp_num:
        if(player_guess > comp_num):
            guess_count += 1
            print("You are to high!")
            player_guess = float(input("What number did comp choose?: "))
        if(player_guess < comp_num):
            guess_count += 1
            print("You are to low!")
            player_guess = float(input("What number did comp choose?: "))
    guess_count += 1
    print(player_name + ", YOU GUESSED IT!  It took you", guess_count, "tries.")

def keep_going():
    select = input("Want to play y/n: ")
    return select

def main():
    continues = ''
    while continues != "n":
        if continues == "y":
            game_guess()
            continues = keep_going()
        else:
            continues = keep_going()
main()