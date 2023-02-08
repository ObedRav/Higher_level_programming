# Write a Python program that accepts a sequence of comma-separated 
# numbers from the user and generates a list and a tuple of those numbers
#!/usr/bin/python3

data_from_user = input("Enter the sequence: ")
list_data_from_user = list(data_from_user.split(", "))
tuple_data_from_user = tuple(list_data_from_user)
print(f"List: {list_data_from_user}\nTuple: {tuple_data_from_user} ")