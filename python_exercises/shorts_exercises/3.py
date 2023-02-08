#Write a Python program to display the current date and time.
#!/usr/bin/python3

import datetime


current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time : \n", current_time)