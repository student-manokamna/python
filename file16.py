
'''
16. Write a program in python that counts the frequency of each character in
a string.
'''

input_string = input("Enter a string: ")

# below is  an empty dictionary to store character frequency
freq = {}

# to count frequency of char
for char in input_string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Frequency of each character:")
for char, freq in freq.items():
    print(char + ":", freq)
