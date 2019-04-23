def collatz(number):
    if number % 2 == 0:
        print(number //2)
        return number // 2
    elif number % 2 ==1:
        print(3 * number + 1)
        return 3 * number + 1
    elif number == 1:
        return 1


print("Enter number:")
global entry
try:
    entry = int(input())
except ValueError:
    print("Enter an integer.")

while entry != 1:
    entry = collatz(entry)