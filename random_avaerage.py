#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on Decemebr 2020
# This program generates 10 random numbers and calculates their average

import random


def main():
    # this function generates 10 random numbers and calculates their average

    my_numbers = []
    total = 0

    # generates numbers, stores them in list, prints them
    for loop_counter in range(0, 10):
        random_number = random.randint(1, 100)
        my_numbers.append(random_number)
        print("Random number: {0}".format(random_number))

    # find total of random numbers
    for loop_counter in range(0, 10):
        total = total + my_numbers[loop_counter]

    # calculate average from total
    average = total / 10

    print("Average: {0}".format(average))


if __name__ == "__main__":
    main()
