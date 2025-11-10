#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: October 2025
# This program checks if the year given by user is a leap year


def main():
    try:
        print("Welcome to the Package  Check Program!")

        # get inputs
        weight = float(input("Enter weight (kg): "))
        length = float(input("Enter length (cm): "))
        width = float(input("Enter width (cm): "))
        height = float(input("Enter height (cm): "))

        # calculate volume
        volume = length * width * height

        # nested if statements
        if weight > 0 and length > 0 and width > 0 and height > 0:
            # check if weight is less or equal to 27kg
            if weight <= 27:
                # check if volume is less or equal to 10000
                if volume <= 10000:
                    print("Your package is valid for shipping!")
                else:
                    print("Sorry, the volume is too large to ship.")
            else:
                print("Sorry, this package is too heavy to ship.")
        else:
            print("Invalid input. Enter a positive number.")

        # ask user if they want to check another package
        userAnswer = input("Do you want to check another package? (yes or no): ")

        if userAnswer == "yes":
            print("Okay! Restart the program to check another package.")
        else:
            if userAnswer == "no":
                print("Okay! Have a great day!")
            else:
                print("Invalid answer. Please type yes or no.")
    # exception handling
    except ValueError:
        print("ERROR. Enter a valid input")
    # end program
    finally:
        print("Thanks, have a good day.")


if __name__ == "__main__":
    main()
