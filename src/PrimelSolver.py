# -*- coding: utf-8 -*-
"""
A solver for Primel, a game where you are given 6 attempts to
guess a 5-digit prime, with "hints" given along the way:
https://converged.yt/primel/

Note that while there is a reasonable amount of user validation
included, if one really desired, then it's still possible to
intentionally throw errors.
"""
import re
from itertools import permutations


def is_prime(n: int) -> bool:
    """Check primality of n."""
    if not isinstance(n, int) or n < 2:
        return False
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True


def digit_repeater(digits: list, repetition_amount: int) -> list:
    """Return a list of digits, with repetition."""
    repeated_digits = []
    for digit in digits:
        for _ in range(repetition_amount + 1):
            repeated_digits.append(digit)
    return repeated_digits


def int_tuple_concatenator(numbers: tuple) -> int:
    """Convert a tuple of integers into a concatenated integer."""
    integer_as_string = ""
    for number in numbers:
        integer_as_string += str(number)
    return int(integer_as_string)


def candidate_primes(admissible_digits: list) -> list:
    """Return a list of all 5-digit primes, from a given list of digits."""
    admissible_digits_repeated = digit_repeater(admissible_digits, 5)
    candidate_set = set(permutations(admissible_digits_repeated, 5))
    candidate_list = [int_tuple_concatenator(candidate_tuple)
                      for candidate_tuple in candidate_set]
    return sorted([p for p in candidate_list if is_prime(p)])


def regex_matches(search_list: list, regex: str, match=True) -> list:
    """Return a list of all matches, of a given list, against a regex.

    An option to include or exclude via the match boolean can be passed.
    """
    match_list = []
    for item in search_list:
        if match and re.search(regex, str(item)):
            match_list.append(item)
        elif match is False and not re.search(regex, str(item)):
            match_list.append(item)
    return match_list


def tuple_string_converter(tuple_string: str) -> tuple:
    """Convert a tuple, written as a string, into a Python tuple."""
    tuple_object = tuple(tuple_string.strip("()").replace(" ", "").split(","))
    return tuple_object


def tuple_to_regex(user_input: str) -> tuple:
    """Convert user input of the form (colour, digit, position) into regex."""
    tuple_object = tuple_string_converter(user_input)
    (colour, digit, position) = (tuple_object[0].upper(),
                                 int(tuple_object[1]), int(tuple_object[2]))
    regex_string = ("." * (position - 1)
                    + str(digit)
                    + "." * (5 - position))
    match = bool(colour == "GREEN")
    return regex_string, match


def tuple_validation(tuple_string: str) -> bool:
    """Validate that tuple_string is of the form (colour, digit, position)."""
    tuple_object = tuple_string_converter(tuple_string)
    if len(tuple_object) != 3:
        return False
    (colour, digit, position) = (tuple_object[0].upper(),
                                 tuple_object[1], tuple_object[2])
    admissible_colours = ["GREY", "YELLOW", "GREEN"]
    admissible_digits = ["0", "1", "2", "3", "4",
                         "5", "6", "7", "8", "9"]
    admissible_positions = ["0", "1", "2", "3", "4", "5"]
    if (colour not in admissible_colours
            or digit not in admissible_digits
            or position not in admissible_positions):
        return False
    return True


# We make two prime guesses which gives us some data on all digits.
# TODO: Improve these guesses by using digit and position frequency analysis.
FIRST_GUESS = 97861
SECOND_GUESS = 50423


def main():
    """Execute the program, with user interaction."""
    print("-" * 50)
    print(f"Obtain initial data by trying {FIRST_GUESS} and {SECOND_GUESS}.\n")
    print("Which digits are not grey? (Separate digits with a space)")
    digit_input = input()
    digit_list = (map(int, digit_input.split()))
    candidate_list = candidate_primes(digit_list)
    while True:
        more_input = "Y"
        while more_input == "Y":
            print("-" * 50)
            print("Enter data in the form (green/yellow, digit, position):")
            print("(Press enter to skip this)")
            digit_data = input()
            if digit_data == "":
                pass
            else:
                while not tuple_validation(digit_data):
                    print("You've made an input typo. Please try again:")
                    digit_data = input()
                (regex, match) = tuple_to_regex(digit_data)
                candidate_list = regex_matches(candidate_list, regex, match)
            print("-" * 50)
            print("Do you have more information to include (Y/N)?")
            more_input = input().upper()
            while more_input not in ("Y", "N"):
                print("You've made a typo - please type Y or N.")
                more_input = input().upper()
        print("-" * 50)
        print(f"Try: {candidate_list.pop(0)}")
        print("Press enter to keep trying. Otherwise, close this window.")
        input()


main()
