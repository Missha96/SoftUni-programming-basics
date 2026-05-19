r = float(input())

from math import pi

circle_area = pi * r * r
perimeter_circle = 2 * pi * r

circle_area_formatted = f"{circle_area:.2f}"
perimeter_circle_formatted = f"{perimeter_circle:.2f}"

print(circle_area_formatted)
print(perimeter_circle_formatted)