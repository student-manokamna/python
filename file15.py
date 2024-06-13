
'''
15. Write a program that reads data from a CSV file and prints it to the
console.
'''

import csv
file_path = input("Enter the path to the CSV file: ")

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
