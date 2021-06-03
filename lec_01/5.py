from math import sqrt
a, b, c = map(int, input().split())
d = b ** 2 - 4 * a * c
if a == 0:
    if b != 0:
        print(-c / b)
    elif b == 0 and c == 0:
        print("Infinite number of solutions")
else:
    if d == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        if (x1 < x2):
            print(x1, x2)
        else:
            print(x2, x1)
    else:
        print("Discriminant is negative")