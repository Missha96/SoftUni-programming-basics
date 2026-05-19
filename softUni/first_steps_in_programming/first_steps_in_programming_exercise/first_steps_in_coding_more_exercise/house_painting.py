x = float(input())
y = float(input())
h = float(input())

# S = x * x лице на квадрата и на правоъгълника в основата
area_square = x ** 2
area_of_rectangle = x * y

#roof лице на двата триъгълника и на двата правоъгълника на покрива
triangle_area = 2 * (x * h /2)
roof_rectangle = 2 * area_of_rectangle

door = 1.2 * 2
window = 2 * (1.5 * 1.5)

#страните без вратата и страните без прозореца
front_and_back = (area_square * 2) - door
side = (area_of_rectangle * 2) - window

green_side = front_and_back + side
red_area = triangle_area + roof_rectangle
litters_of_green_paint = green_side / 3.4
litters_of_red_paint = red_area / 4.3

green_formatted = f"{litters_of_green_paint:.2f}"
red_formatted = f"{litters_of_red_paint:.2f}"

print(green_formatted)
print(red_formatted)