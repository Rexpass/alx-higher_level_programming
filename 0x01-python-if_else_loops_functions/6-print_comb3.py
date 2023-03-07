#!/usr/bin/python3
for a in range(9):
    for b in range(1 + a, 10):
        if a == 8:
            break
        print("{}{}".format(a, b), end=", ")
print("89")
