import csv
import re
from pickle import TRUE
from typing import Counter 

counter = 0

with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"].strip().upper()
        if re.search("^(PYTHON|THE PYTHON)$", language):
            counter += 1

print(f"The number of people who like Python is: {counter}")





















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
