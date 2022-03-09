fahrenheit = float(input("What value of fahrenheit would you like to convert: "))
celsius = round((fahrenheit-32) * (5/9), 1)
print("The converted temperature is " + str(celsius) + " celsius")