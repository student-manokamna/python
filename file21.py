
'''
21. Write a python program that counts the occurrences of a specific element
in a list.
'''
def count_occurrences(lst, element):
    count = 0
    for elements in lst:
        if elements == element:
            count += 1
    return count

numbers = input("Enter a list of numbers separated by space: ").split()

numbers = [int(num) for num in numbers]
element = int(input("Enter the element to count occurrences: "))
occurrences = count_occurrences(numbers, element)
print("Occurrences of", element, "in the list:", occurrences)
