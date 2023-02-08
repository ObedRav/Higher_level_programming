# Write a Python program that accepts a filename
# from the user and prints the extension of the file
#!/usr/bin/python3

filename = input("Enter the filename: ").split(".")
print(filename[-1])