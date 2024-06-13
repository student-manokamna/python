
'''
25. Write a program that copies the contents of one text file to another.
'''
source_file = input("Enter the name of the source file: ")
destination_file = input("Enter the name of the destination file: ")
# destination_file is m.txt
try:

    with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
     
        destination.write(source.read())
    print("File copied successfully!")
except FileNotFoundError:
    print("Error: One of the files does not exist.")
