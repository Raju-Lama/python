# we cannot add elements to a tuple

# we can work around this by converting the tuple to a list, adding the element, and then converting it back to a tuple

tup = (1, 2, 3)

a = list(tup)

a.append(4)

tup = tuple(a)

print(type(tup))