#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program rounds decimal numbers and passes values by reference


def round_decimals(decimal_number, decimal_places):
    # This function rounds the number

    decimal_number[0] = decimal_number[0] * 10 ** decimal_places[0]
    decimal_number[0] = decimal_number[0] + 0.5
    decimal_number[0] = int(decimal_number[0])
    decimal_number[0] = decimal_number[0] * 10 ** -decimal_places[0]


def main():
    # This function gets the number and decimal places to round by
    number = []
    decimals = []

    # Input
    print("This program rounds decimal numbers.")
    print("")
    number_input_string = input("Enter a decimal number to round: ")
    decimals_input_string = input("Enter the number of decimal places to "
                                  "round by: ")

    # Process
    while True:
        try:
            number_input_float = float(number_input_string)

            break
        except Exception:
            number_input_string = input("{} is not a valid input. Enter a "
                                        "decimal number: ".
                                        format(number_input_string))
    while True:
        try:
            decimals_input_integer = int(decimals_input_string)

            if decimals_input_integer >= 0:
                break
            else:
                decimals_input_string = input("Must be a positive integer. "
                                              "Enter the number of decimal "
                                              "places to round by: ")
        except Exception:
            decimals_input_string = input("{} is not a valid input. Enter the "
                                          "number of decimal places to round "
                                          "by: ".format(decimals_input_string))
    number.append(number_input_float)
    decimals.append(decimals_input_integer)

    # Call functions
    round_decimals(number, decimals)

    # Output
    print("")
    print("The rounded number is: {}".format(number[0]))
    print("\nDone.")


if __name__ == "__main__":
    main()
