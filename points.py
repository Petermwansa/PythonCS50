from cs50 import get_int

points = get_int("How many points did you get? ")

if points < 6:
    print("You got less than me")
elif points > 6:
    print("You got more than me")
else:
    print("We got the same number of points")
