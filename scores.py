from cs50 import get_int 
scores = []

for i in range(3):
    score = get_int("Enter the scores of each: ")
    scores += [score]

#this is a little function to determine the average
average = sum(scores) / len(scores)
print(f"average: {average}")