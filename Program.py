import Classes
import time
import random


def print_pause(message_to_print):

    print(message_to_print)
    time.sleep(1)


# Option if player want to play again
def restar_game():
    restart = ["n", "y"]
    valid = False
    while valid is False:
        ask = raw_input("Would you like to play again? y/n... ")
        if ask in restart:
            valid = True
        else:
            print("Opps, not a valid option, Try again... ")
    if ask is "y":
        print_pause("Excellent! Restarting the game ...")
        play()
    else:
        print("THANKS FOR PLAYING! See you next time.")
        exit()


def play():
    r = random.randint(1, 4)
    p2 = Classes.Player()
    if r is 1:
        p2 = Classes.RandomPlayer()
    elif r is 2:
        p2 = Classes.ReflectPlayer()
    elif r is 3:
        p2 = Classes.CyclePlayer()
    else:
        Classes.Player()
    p1 = Classes.Human_Player()
    print_pause(u"WELCOME to \u001b[31;1mRock \u001b[32;1mPa\
per \u001b[33;1mScissors,\u001b[0m")
    v = True
    while v is True:
        rounds = raw_input("How many rounds do you want to play? ")
        try:
            rounds = int(rounds)
            v = False
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    partida = Classes.Game(p1, p2)
    partida.play_game(rounds)
    restar_game()


play()
