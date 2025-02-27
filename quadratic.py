import math

a = float(input('Enter the value for a '))
b = float(input('Enter the value for b '))
c = float(input('Enter the value for c '))

result1 = (-b + math.sqrt(b**2 - 4 * a * c))/(2 * a)
result2 = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)

print('Roots are ', result1, result2) 