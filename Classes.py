#!/usr/bin/env python3
import random
import time


def print_pause(message_to_print):

    print(message_to_print)
    time.sleep(1)


plays = ['rock', 'paper', 'scissors']


# """This program plays a game of Rock, Paper, Scissors between two Players,
# and reports both Player's scores each round."""
#
# """The Player class is the parent class for all of the Players
# in this game"""
# All posibles ways computer can play this game PLAYER 2
class Player:
    def move(self, remember, round_number):
        # Opponent JUST PLAYS rock
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Opponent takes a random desition
class RandomPlayer(Player):
    def move(self):
        return random.choice(plays)


# Opponent remember last move of the player
class ReflectPlayer(Player):
    def move(self, remember, round_number):
        if remember == "paper":
            return "scissors"
        elif remember == "scissors":
            return "rock"
        else:
            return "paper"


# Opponent cycles through the three moves
class CyclePlayer(Player):
    def move(self, remember, round_number):
        return plays[round_number]


# Ways to win
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Human player class how depent also of Class player
class Human_Player(Player):
    def move(self):
        valid = False
        while valid is False:
            play = raw_input("Rock, paper, scissors? GO!... ")
            if play.lower() in plays:
                valid = True
                return play.lower()
            else:
                print("Opps, not a valid option, Try again... ")


# Play the whole game
class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

# Play just one round
    def play_round(self, remember, round_number):
        move1 = self.p1.move()
        move2 = self.p2.move(remember, round_number)
        print("You played: " + str(move1).upper() + " \n"
              "Opponent played: "+str(move2).upper())
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        result = []
        if move1 == move2:
            print(u"\u001b[43;1m--- TIE ---\u001b[0m\n")
            result.append("TIE")
            result.append(move1)
            return result
        else:
            if beats(move1, move2) is True:
                print(u"\u001b[44;1m** YOU WIN **\u001b[0m\n")
                result.append("P1")
                result.append(move1)
                return result
            else:
                print(u"\u001b[41;1m-- YOU LOSE --\u001b[0m\n")
                result.append("P2")
                result.append(move1)
                return result
        remember = move1

# Function that gives the instroction to play all rounds
    def play_game(self, rounds):
        Score1 = 0
        Score2 = 0
        print(u"\u001b[34;1mGame start!\n")
        print_pause("3")
        print_pause("2")
        print_pause("1")
        print_pause("GO....")
        print_pause(u'\u001b[0m')
        remember = "rock"
        round_number = 0
        for round in range(rounds):
            print_pause(u'\u001b[45;1mROUND ' + str(round+1) + u'\u001b[0m')
            if round_number == 3:
                round_number = 0
            winner = self.play_round(remember, round_number)
            remember = winner[1]
            if winner[0] == "P1":
                Score1 += 1
            elif winner[0] == "P2":
                Score2 += 1
            else:
                Score1 += 0
                Score2 += 0
            round_number += 1

        print(u"\u001b[32;1mSCORE: YOU= " + str(Score1) + " OPPONENT= \
" + str(Score2) + u"\u001b[0m")
        if Score1 > Score2:
            print(u"\u001b[44;1mCONGRATULATIONS YOU WIN \
THIS MATCH!!\u001b[0m\n")
        elif Score2 > Score1:
            print(u"\u001b[41;1mSorry you lose this time, \
Keep trying\u001b[0m\n")
        else:
            print(u"\u001b[43;1mIts a TIE!\u001b[0m\n")


if __name__ == '__main__':
    game = Game(Player(), Player())
