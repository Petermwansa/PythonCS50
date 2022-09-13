from cs50 import get_int

checker = get_int("Enter the number that you want to check: ")

if checker % 2 == 0:
    print("Even")
else:
    print("Odd") 