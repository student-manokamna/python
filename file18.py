
'''
18. Write a python program that checks if two strings are anagrams of each
other
'''

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()
sorted_string1 = sorted(string1)
sorted_string2 = sorted(string2)
if sorted_string1 == sorted_string2:
    print("The strings anagrams.")
else:
    print("The strings  not anagrams.")
