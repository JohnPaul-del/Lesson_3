
numbers = {"one": "один", "two": "два", "three": "три",
           "four": "четыре", "five": "пять", "six": "шесть",
           "seven": "семь", "eight": "восемь", "nine": "девять",
           "zero": "ноль"}


def num_translate(number):
    """
    Translate from English to Russian the name of numbers.

    :param number: Name of number in English
    :return: The value of key
    """
    if number.istitle() and number.lower() in numbers:
        return numbers.get(number.lower()).title()
    return numbers.get(number)


print(num_translate(input("Введите число на английском: ")))
