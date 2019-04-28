multi = """Multi
line
string"""

print(multi)

spam = 'Hello world!'
print(spam.upper())
print(spam.lower())

feeling = input("How are you (great)?\n")
if feeling.lower() == 'great':
    print("I feel great too!")
else:
    print("So you're {}? Okay.".format(feeling.title()))

'hello'.isalpha()
'hello12333'.isalpha()
'hello12333'.isalnum()

'   '.isspace()
'Title Case'.istitle()
'Helloworld!'.startswith("H")
'Helloworld!'.endswith("!")


print('   center justified   '.center(40, '-'))
print('   right justified   '.rjust(40, '-'))
print('   center justified   '.lstrip().center(40, '-'))
