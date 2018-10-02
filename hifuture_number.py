"""hifuture_number.py: Check if a given number satisfies HiFuture's content Software conditions"""


__author__ = "Roberto Gallotta"


import math


# Method to return the nth digit (right to left)
def get_nth_digit(number, n):
    return number // 10**n % 10

# O(n) solution; could not find a reliable algorithm to make a O(1) one
def check_number(num):
    digits = int(math.log10(num)) + 1
    if digits < 2:
        return False # just to be sure; if num has always at least 2 digit, this check could be removed
    for i in range(digits - 1):
        if abs(get_nth_digit(num, i) - get_nth_digit(num, i+1)) != 1: # quick iteration
            return False
    return True


if __name__ == '__main__':
    num = abs(int(input("Type a number: "))) # no negative numbers allowed
    if check_number(num):
        print("HiFuture guys like " + str(num) + "\n")
    else:
        print("HiFuture guys don't like " + str(num) + "\n")
