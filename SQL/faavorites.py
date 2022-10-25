import csv 

languages = []

with open("favourites.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if not row["language"] in languages:
            languages.append(row["language"])



for language in languages:
    print(language)


