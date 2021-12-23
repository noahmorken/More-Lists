cubes = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    cubes.append(value**3)

print(cubes)

cubes = [value**3 for value in range(1, 11)]
print(cubes)