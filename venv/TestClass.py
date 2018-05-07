print("This is python")

x = 10
z = 20

if z > x:
    print('Hello')
else:
    print('Not Hello')

c = x + z  # Addition

d = 15 / 5
e = 15 // 5
f = 15 % 5

print("Addition " + str(c))
print("Discards Fractional part " + str(e))
print("Reminder " + str(f))

import math

abc = math.sqrt(2)
print(abc)
print('Square Root of 5 * 3 is ' + str(5 ** 3))

List = [1, 2, 3, 4, 5] + [20, 30, 40]

print('List ' + str(List[:]))

# Fibonnaci Series

a, b = 0, 1
while (b < 10):
    print("fibonacci " + str(b))
    a, b = b, a + b
