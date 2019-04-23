def spam(divideBy):
    return 42/divideBy

def spam_fixed(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Division by zero... Invalid value')


print(spam(2))
print(spam(12))
print(spam_fixed(0))
print(spam(1))

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error, invalid argument.')