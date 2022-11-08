# Python append
# What will be the output?

def func(x, y = [20, 50]):
    y.append(x)
    return y

print(func(2, [50, 20]))

# Output
# [50, 20, 2]

# Parameter y has a default value of [20, 50] which is optional during function call
# but in func(), value for y is provided as [50, 20] so it will be overwrite the default value.

