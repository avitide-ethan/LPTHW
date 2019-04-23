def convert(entry):

    string = ", ".join(map(str, entry[:-1])) \
             + ", and {}".format(entry[-1])
    return string

print(convert(['a', 2, 3]))

# input("Enter a list."))



