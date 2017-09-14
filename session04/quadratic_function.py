import math


def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c  # calculate the discriminant

    if discriminant >= 0:  # equation has solutions
        x_1 = ((-b + math.sqrt(discriminant)) / 2 * a)
        x_2 = ((-b - math.sqrt(discriminant)) / 2 * a)
        return x_1, x_2

    else:
        print('No Real Number Solution.')
        return None


# print(quadratic(2,2,2))
# print(quadratic(1,4,1))

a = float(input('please enter a number:'))
b = float(input('please enter a number:'))
c = float(input('please enter a number:'))
print('Results are:', quadratic(a, b, c))
