def print_two(*args):
    arg1, arg2 = args
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_two_again(arg1, arg2):
    print("arg1: {}, arg2: {}".format(arg1, arg2))

def print_one(arg1):
    print("arg1: {}".format(arg1))

def print_none():
    print("Got nuthin' doe.")

print_two("Ethan", "Doe")
print_two_again("Ethan", "Doe")
print_one("One")
print_none()
