import random

def luhn_checksum(card_number):
    def digits_of(n): return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def generate_card_number(bin_prefix, length=16):
    card = bin_prefix
    while len(card) < (length - 1):
        card += str(random.randint(0, 9))
    for i in range(10):
        check_digit = str(i)
        if luhn_checksum(card + check_digit) == 0:
            return card + check_digit
    return None
