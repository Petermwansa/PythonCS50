import csv
import sqlite3
import re
from pickle import TRUE
from typing import Counter 
from cs50 import SQL


# here we have opened the fav db filew by inporting csv into sqlite
db = SQL("sqlite:///favorites.db")


# prompt the user to enter the tilte 
language = input("Language: ").strip()

# execute the sql query on the db it returns the count as the list of rows
rows = db.execute("SELECT COUNT(*) AS counter FROM favorites WHERE language LIKE ?", language)

row = rows[0]


print(row["counter"])
















# MAKE THE USER ENTER THE TITLE THEY WANT TO SEARCH FOR 

# we prompt the user to enter 
# language = input("Language: ").strip().upper()

# counter = 0

# with open("favourites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if row["language"].strip().upper() == language:
#             counter += 1

# print(counter)





# PRINT OUT A TITLE TO THE SCREEN 

# counter = 0

# with open("favourites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         language = row["language"].strip().upper()

#         # here we are using regular expresions to check that the user has input from the beggining of the senntence and doesnot type anything at the end "$"
#         if re.search("^(PYTHON|THE PYTHON)$", language):
#             counter += 1

# print(f"The number of people who like Python is: {counter}")





















# ========================       THE CODE FOR COLLECTING THE DATA AND SORTING OUT AND GROUPING IT =============== 


# import csv
# from pickle import TRUE 

# languages = {}

# with open("favourites.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         language = row["language"].strip().upper()
#         if language in languages:
#             languages[language] += 1
#         else:
#             languages[language] = 1


# # we sort out, then we use the get_value function then we reverse the returned data 
# #the lambda function enables you to create a function that you can use just once off and that is all and throw it away
# for language in sorted(languages, key=lambda language: languages[language], reverse=True):
#     print(language, languages[language])
