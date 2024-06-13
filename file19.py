
'''
19. Write a python program that removes all punctuation from a given string
'''
import string
def remove_punctuation(input_string):
    translator = str.maketrans("", "", string.punctuation)
    return input_string.translate(translator)
input_string = input("Enter a string: ")
cleaned_string = remove_punctuation(input_string)

print("String without punctuation:", cleaned_string)
