def add(a, b):
    print(f"ADDING {a} + {b}")
    return a+b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a-b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a*b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a/b



print("Let's do some math wit da functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here's a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, " divide 100/2 = 50. divide 50/2 = 25.")
print("multiply 90 *2 = 180. multiply 180*25 = 4500. 78-4 = 74. 74 - 4500 = -4426. add 35 + -4426 = ???")




print(divide(add(add(add(44, 56), add(72, 80)), 92), 5))
print(divide(add(add(add(44, 46), add(50, 60)), 65), 5))

print(divide(add(24, 34), subtract(100, 1023)))
