def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have {} cheeses!".format(cheese_count))
    print("You have {} boxes o' crackers".format(boxes_of_crackers))
    print("Man, that's enough for a party! \nGet a blanket.\n")

print("We can give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("Can do math inside too.")
cheese_and_crackers(10 + 20, 5 + 6)

def add_multiply(x, y):
    print("x = {}, y = {}".format(x, y))
    print("x + y = {}".format(x+y))
    print("x * y = {}".format(x*y))
    print("Done")

add_multiply(1, 1)

a, b, c, d = 1, 2, 3, 4
z = add_multiply(a, b)
z
add_multiply(c, d)
