area_square = lambda side: side * side
area_rectangle = lambda length, width: length * width
area_triangle = lambda base, height: 0.5 * base * height
side = 5
length = 6
width = 4
base = 8
height = 3

print(f"Area of square: {area_square(side)}")
print(f"Area of rectangle: {area_rectangle(length, width)}")
print(f"Area of triangle: {area_triangle(base, height)}")
