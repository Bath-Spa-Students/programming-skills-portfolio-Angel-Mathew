## Exercise 3: Print date and Time :ballot_box_with_check:Write a Python program to display the current date and time.
import datetime
now=datetime.datetime.now()
print("current date and time:")
print(now.strftime("%y-%m-%d %H:%M:%S"))