buffet = ('enchiladas', 'cookies', 'bagels', 'chicken drumsticks', 'salmon')

print("Food items at the buffet:")
for food in buffet:
    print(food)

# buffet[0] = 'cake' (Failure)

buffet = ('cake', 'eggs', 'bagels', 'chicken drumsticks', 'salmon')
print("\nRevised food items at the buffet:")
for food in buffet:
    print(food)