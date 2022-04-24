#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 20, 2022
# This program asks the user to enter a number. It then displays the
# power of two of each number from 0 until that number using for loops.


def main():
    # initialize the loop counter and power_of_two
    counter = 0
    power_of_two = 0

    # get the user number as a string
    user_number_string = input("Enter a whole number: ")
    print("")

    try:
        # converts user input to integer
        user_number_int = int(user_number_string)
        # calculate the power of counter using a for loop.
        if user_number_int >= 0:
            for counter in range(user_number_int + 1):
                power_of_two = counter**2
                print("{}^2 = {}".format(counter, power_of_two))
                counter = counter + 1

        else:
            print("{} is not a whole number".format(user_number_int))
    except Exception:
        print("{} is not a valid number.". format(user_number_string))


if __name__ == "__main__":
    main()
