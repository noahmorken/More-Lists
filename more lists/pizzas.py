pizzas = ['all meat', 'deluxe', 'hawaiian chicken']
for pizza in pizzas:
    # print(pizza.title())
    print(f"I like the {pizza.title()} from Marco's Pizza!")

print("\nThank you for buying it for us!")

friend_pizzas = pizzas[:]
friend_pizzas.append('garden')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())