#!/usr/bin/env python3.7

fahrenheit = float(input("What value of fahrenheit would you like to convert to celsius?: "))
celsius = round((fahrenheit-32) * (5/9), 1)
print(str(fahrenheit) + "F is", str(celsius) + "C")