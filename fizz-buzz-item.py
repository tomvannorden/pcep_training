#!/usr/bin/env python3.7

user_input = input("Please type a random number?: ")
number = int(user_input)
print(number)

if (number % 3 == 0) and (number % 5 == 0):
    print("FizzBuzz")
elif (number % 3) == 0:
    print("Fizz")
elif (number % 5) == 0:
    print("Buzz")
else:
    pass
