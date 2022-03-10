#!/usr/bin/env python3.7

user_input = input("Please type a random string?: ")

print("First character of string: " + str(user_input[0]))
print("Last character of string: " + str(user_input[-1]))
print("Middle character of string: " + str(user_input[int((len(user_input)-1)/2)]))
print("Even index characters of string: " + str(user_input[0::2]))
print("Uneven index characters of string: " + str(user_input[1::2]))
print("String in reverse: " + str(user_input[::-1]))