from math import pi

figure_type = input()

if figure_type == "square":
    square_side = float(input())
    square_area = square_side * square_side
    square_formatted = (f"{square_area:.3f}")
    print(square_formatted)
elif figure_type == "rectangle":
    rectangle_side = float(input())
    rectangle_side2 = float(input())
    rectangle_area = rectangle_side * rectangle_side2
    rectangle_formatted = (f"{rectangle_area:.3f}")
    print(rectangle_formatted)
elif figure_type == "circle":
    r = float(input())
    circle_area = pi * r * r
    circle_formatted = (f"{circle_area:.3f}")
    print(circle_formatted)
elif figure_type == "triangle":
    triangle_side = float(input())
    triangle_high = float(input())
    triangle_area = (triangle_side * triangle_high) / 2
    triangle_formatted = (f"{triangle_area:.3f}")
    print(triangle_formatted)
