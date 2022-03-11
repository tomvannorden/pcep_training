#!/usr/bin/env python3.7

user_input = input("Please type a random string?: ")

lower = user_input.lower()
print(lower)

upper = user_input.upper()
print(upper)

title = user_input.title()
print(title)

capitalize = user_input.capitalize()
print(capitalize)

separate = user_input.split()
print(separate)


ord_separate = separate.sort()
print(type(ord_separate))

sorted_separate = sorted(separate)
print(type(sorted_separate))

print(sorted_separate[0])
print(sorted_separate[-1])
