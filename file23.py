
'''
23. Write a program that converts temperature from Celsius to Fahrenheit
and vice versa based on user input.
'''
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of temperature (C for Celsius, F for Fahrenheit): ")
if unit.upper() == 'C':
    converted_temperature = (temperature * 9/5) + 32
    print(f"{temperature}°C is equal to {converted_temperature}°F")
elif unit.upper() == 'F':
    converted_temperature = (temperature - 32) * 5/9
    print(f"{temperature}°F is equal to {converted_temperature}°C")
else:
    print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
