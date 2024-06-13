
'''
12. Write a python program that calculates the sum of the digits of a given
number.
'''

number = input("Enter a number: ")


total_sum = 0

for digit in number:
    total_sum += int(digit)

print("The sum of digits of", number, "is:", total_sum)
