from cs50 import get_string 
import csv



#THE CSV FILE 

name = get_string("Enter the name:  ")
number = get_string("Enter the number:  ")

with open("phonebook.csv", "a") as file:

    writer = csv.writer(file)
    writer.writerow([name, number])






#USING LINEAR SEARCH

#people = {
#    "Peter": "+7-900-465-4587",
#    "Moses": "+26-900-465-4587",
#    "Brian": "+26-900-466-6777"

#}

#name = get_string("Enter the name of the person:  ")

#if name in people:
#    number  = people[name]
#    print(f"Number: {number}")