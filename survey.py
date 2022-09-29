import csv 

countries = {
    "UK": 0,
    "Zambia": 0,
    "Brazil": 0,
    "India": 0,
    "USA": 0
}

with open("survey.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        country = row["Country"]
        countries[country] += 1

for country in countries:
    count = countries[country]
    print(f"{country}: {count}")


