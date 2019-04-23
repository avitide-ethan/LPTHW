spam = ['cat', 'bat', 'rat', 'elephant']

spam[-1] = 'elephant'
spam[-3] = 'bat'

print(spam)
print(spam[0:-1])

spam += spam
print(spam)
del spam[4:8]

for i in range(len(spam)):
    print(f"Index {i} in spam is: {spam[i]}!!!")

if 'cat' in spam:
    print("'cat' is in spam!")

a, b, c, d = spam
print(b)
a, b, c, d = d, c, b, a
print(f"After swapping everything b is now equal to {b}.")

print("The value 'cat' is located at index {}.".format(spam.index('cat')))
spam.append('cat')
print("The FIRST value 'cat' is located at index {}.".format(spam.index('cat')))
spam.insert(spam.index('cat'), 'not cat')
print(spam)
spam.remove('cat')
spam.append('Cat')
print("Removed 'cat' from the list, added a 'Cat'")
spam.sort(reverse=True, key=str.lower)
print(spam)

