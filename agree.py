from cs50 import get_string 

s = get_string("Dop you agree? Y/N  ").lower()

if s in ["Y", "yes"]:
    print("Agreed!!!")

elif s in ["N", "no"]:
    print("Did not agree!!!")