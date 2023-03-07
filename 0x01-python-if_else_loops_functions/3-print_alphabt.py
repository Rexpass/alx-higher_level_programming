#!/usr/bin/python3
letter = 97
for letter in range(97, 123):
    if letter == 101 or letter == 113:
        continue
    print("{}".format(chr(letter)), end='')

