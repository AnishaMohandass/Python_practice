# Python sep parameter
# What will be the output?

# The sep parameter is primarily used to format the strings that need to be printed on the console
# and add a separator between strings to be printed.
# The default value for sep is whitespace.

Dict = {1:2, 3:4}

# with sep parameter
for i, j in Dict.items():
    print(i, j, sep="→")

# without sep parameter
for i, j in Dict.items():
    print(i, j)


# Output
# 1→2
# 3→4
# 1 2
# 3 4

