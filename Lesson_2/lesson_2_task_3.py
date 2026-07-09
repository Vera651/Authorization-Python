import math

def square(side):
    area = side * side
    return math.ceil(area)

num_side = int(input("Введите длину стороны: "))
result = square(num_side)
print(f"Площадь квадрата: {result}")
