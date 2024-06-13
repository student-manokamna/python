
'''
20. Write a python program that takes a list of numbers and returns their sum.
'''

def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum
numbers = input("Enter a list of numbers separated by space: ").split()
numbers = [int(num) for num in numbers]
result = calculate_sum(numbers)
print("Sum of the numbers:", result)

