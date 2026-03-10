# Значение радиуса круга
radius = 42

# Вычисляем площадь круга
pi = 3.1415926
area = pi * radius ** 2
print(round(area, 4))


point_1 = (23, 34)

distance_1 = (point_1[0] ** 2 + point_1[1] ** 2) ** 0.5

print(distance_1 <= radius)


point_2 = (30, 30)

distance_2 = (point_2[0] ** 2 + point_2[1] ** 2) ** 0.5

print(distance_2 <= radius)