place_words_sub_ten = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
place_words_teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
                     "nineteen"]
place_words_sub_hundred = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

place_words_hundred_plus = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion",
                            "sextillion", "septillion", "octillion", "nonillion", "decillion", "undecillion",
                            "duodecillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion",
                            "quindecillion", "sexdecillion", "septendecillion", "octodecillion", "novemdecillion",
                            "vigintillion", "bajillion"]


def stringify(number):
    """Converts integer to string of number words.
    e.g. 75025 converts seventy five thousand twenty five
    Maximum accuracy is to 10^63 (vigintillion). Anything after that is arbitrarily a bajillion.

    :param number: Integer value
    :return: Number converted to number words or "Input must be integer." if number is not integer
    """
    if number == 0:
        return "zero"
    if isinstance(number, int):
        pass
    else:
        message = "Input must be integer."
        print(message)
        return message

    number_map = _split_number(number)
    number_string = ""
    for place in number_map.keys():

        number_list = number_map[place]
        sub_hundred_string = _build_sub_hundred_number(number_list)
        if place == 0:
            number_string = sub_hundred_string
        else:
            if place >= len(place_words_hundred_plus):
                place = len(place_words_hundred_plus) - 1
            number_string = sub_hundred_string + " " + place_words_hundred_plus[place] + " " + number_string

    return (number_string)


def _build_sub_hundred_number(number_list):
    """Internal function: Converts a number from 0-999 to the words for those numbers.
    e.g. [3, 5, 4] converts to three hundred fifty four

    :param number_list: A list of single digit numbers in the order they are to appear.
    :return: A string of number words
    """
    sub_hundred_string = ""
    first_number = number_list[0]
    second_number = number_list[1]
    third_number = number_list[2]

    if first_number > 0:
        hundreds_place = place_words_sub_ten[first_number] + " hundred"
    else:
        hundreds_place = ""
    ones_place = place_words_sub_ten[third_number]
    tens_place = ""

    if second_number == 0:
        tens_place = ""
    elif second_number == 1:
        ones_place = ""
        tens_place = place_words_teens[third_number]
    else:
        tens_place = place_words_sub_hundred[second_number]

    sub_hundred_string = hundreds_place + " " + tens_place + " " + ones_place
    return sub_hundred_string


def _split_number(number):
    """Internal function: Converts an integer into a dictionary of three digit places.
    e.g. 267914296 converts to {0: [2, 9, 6], 1: [9, 1, 4], 2: [2, 6, 7]}
    The value for place runs lowest to highest based on least significant digits.
    0: 0-999
    1: 0-999 x 10^3
    2: 0-999 x 10^6
    3: 0-999 x 10^9

    :param number: An integer value
    :return: A dictionary of three digit places keyed with the position of that place
    """
    digit_list_full = _convert_number_to_list(number)
    num_digits = len(digit_list_full)

    place_count = 0
    digit_index = 2
    digit_list_place = [0, 0, 0]
    places_map = {}
    #loading numbers into 3-digit arrays back to front
    for d in range(1, num_digits + 1):

        digit_list_place[digit_index] = digit_list_full.pop()

        digit_index -= 1

        if d % 3 == 0:
            places_map[place_count] = digit_list_place.copy()
            place_count += 1
            digit_index = 2

            digit_list_place = [0, 0, 0]

    if len(digit_list_place) > 0:

        has_numbers = False
        for number in digit_list_place:
            if number != 0:
                has_numbers = True
        if has_numbers:
            places_map[place_count] = digit_list_place.copy()

    # print(places_map)

    return places_map


def _convert_number_to_list(number):
    """Internal function: Converts an integer to a list of single digits
    :param number: An integer value
    :return: A list of digits of that integer in the same order
    """
    digit_list_full = list()
    digits_as_string = str(number)
    for digit_string in digits_as_string:
        digit_list_full.append(int(digit_string))

    return digit_list_full
