def rectangle_area(length, width):
    return length * width


def circle_area(radius):
    PI = 3.14
    return PI * (radius ** 2)


length = int(input())
width = int(input())

print(f"The area of the rectangle is: {rectangle_area(length, width)}")

radius = int(input())
print(f"The area of the circle is: {circle_area(radius)}")
