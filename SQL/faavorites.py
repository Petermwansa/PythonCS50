import csv 

languages = set()

with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        language = row["language"].strip().upper()
        languages.add(language)



for language in languages:
    print(language)


