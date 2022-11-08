# Python zip
# What will be the output?

# The zip() function returns a zip object, which is an iterator of tuples
# where the first item in each passed iterator is paired together,
# and then the second item in each passed iterator are paired together etc.

# If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for y in zip(*x):
    print(y, end="")

# Output
# (1, 4, 7)(2, 5, 8)(3, 6, 9)
