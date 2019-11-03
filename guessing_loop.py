#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This plays the random number guessing game with a loop


import random


def main():

    random_int = random.randint(1, 10)
    # this function compares the random_int and value_1
    while True:
        value_1 = input("Guess an integer of your choice ")
        print("")
        try:
            # input
            value_1_int = int(value_1)
            # process and output
            print("")
            if value_1_int == random_int:
                print("You guessed correctly! The number was: " + str(value_1))
                break
            else:
                print("You guessed incorrectly. Try again.")
        except Exception:
            print("Please input only valid integers")


if __name__ == "__main__":
    main()
