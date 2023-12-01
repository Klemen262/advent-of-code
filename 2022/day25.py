from input25 import data

snafu_numbers = data.split("\n")

value = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
chars = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}

def snafu_to_dec(number_as_string):
    i = len(number_as_string) - 1
    number = 0
    power = 1
    while i >= 0:
        number += power * value[number_as_string[i]]
        power *= 5
        i -= 1
    return number

def dec_to_snafu(number):
    snafu_digits = []
    while number > 0:
        snafu_digits.append(number % 5)
        number //= 5
    for i in range(len(snafu_digits) - 1):
        snafu_digits[i + 1] += (snafu_digits[i] + 2) // 5
        snafu_digits[i] = (snafu_digits[i] + 2) % 5 - 2
    return "".join([chars[a] for a in snafu_digits[::-1]])

sum = 0
for snafu in snafu_numbers:
    a = snafu_to_dec(snafu)
    sum += a

print(dec_to_snafu(sum))