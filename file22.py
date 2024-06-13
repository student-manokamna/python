
'''
22. Write a python program that returns the minimum and maximum values
in a list of numbers.
'''

numbers = input("Enter a list of numbers sep by space: ").split()
numbers = [int(num) for num in numbers]
minimum = min(numbers)
maximum = max(numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)

