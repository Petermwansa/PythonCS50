import csv
from pickle import TRUE 

languages = {}

with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"].strip().upper()
        if language in languages:
            languages[language] += 1
        else:
            languages[language] = 1

# this function will the input and return a corresponding value 
def get_value(language):
    return languages[language]

# we sort out, then we use the get_value function then we reverse the returned data 
for language in sorted(languages, key=get_value, reverse=True):
    print(language, languages[language])


