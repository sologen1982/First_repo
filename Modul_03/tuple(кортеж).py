point = (1, 3, 2)           # (  ) кортеж, tuple   ...... [  ]  список, list        {  } словарь  ....... dict

print(f'Tuple: {point}')

print(f"X: {point[0]}")
print(f"Dimension ammount: {len(point)}")

_, y, z = point

print(f"Y: {y}: Z: {z}")

coordinates = "Coordinates: "

for i in point:
    coordinates += f"{i};"

print(coordinates)

