import random
def main():
    player_name = input("Hello, what is your name: ")

    comp_num = random.randint(1,100)

    def game_guess():
        guess_count = 0
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
        print(player_name + ", YOU GUESSED IT!  It took", guess_count, "tries.")


    game_guess()
main()