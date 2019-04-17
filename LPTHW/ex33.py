
def counting_list(number, increment):

    i = 0
    numbers = []
    while i < number:
        print(f"At the top of the loop i is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom of the loop i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


# counting_list(23, 2)


def counting_list_for(number, increment):
    numbers = []
    for i in range(0, number, increment):
        print(f"At the top of the loop i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom of the loop i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


counting_list_for(23, 2)
