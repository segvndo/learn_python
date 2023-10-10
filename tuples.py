# tuples similar to lists, but cannot be changed in any way
# uses () to convery immutability

numbers = (1, 2, 3)
# numbers[0] = 10
print(numbers[0])
# results in error because value of index 0 cannot be changed to 10

# Unpacking
coordinates = (1, 2, 3)
# instead of 
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

x, y, z = coordinates
print(coordinates)
print(x)
# result in 1
print(z)
# result in 3