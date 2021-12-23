million_list = list(range(1, 1000001))
for value in million_list:
    print(value)

print("The first three items in the list are:")
print(million_list[:3])

print("\nThree items from the middle of the list are:")
print(million_list[499998:500001])

print("\nThe last three items in the list are:")
print(million_list[-3:])