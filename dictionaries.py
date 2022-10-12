
pizzas = {
    "cheese": 8,
    "Pepperoni": 9,
    "Beef": 5,
    "Chicken": 9,
    "Pork": 7,
    "Magarita": 10,
    "BBQ": 7
    
    }

for pie, price in pizzas.items():
    print(price)


print("===============  To get the prices of each pizza  =================")
print("=========================================")

for pie1, price1 in pizzas.items():
    print("A whole {} pizza costs ${}".format(pie1, price1))