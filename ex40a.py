import myStuff

myStuffDict = {'apple': "I am APPLES!"}
# print(mystuff['apple'])

myStuff.apple()

print("What's going on")

print(myStuff.tangerine)

print("""
myStuff['apple'] # get apple from DICT
myStuff.apple() # use function apple from myStuff module
""")


class MyStuffy(object):

    def __init__(self):
        print("A new instance of myStuff has initialized! HellooOOOO!")
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am CLASSY APPLES!")


thing = MyStuffy()
thing2 = MyStuffy()
thing.apple()
print(thing.tangerine)

# dict style
print(myStuffDict['apple'])

# module style
myStuff.apple()

# class style
thingy = MyStuffy()
thingy.apple()
print(thingy.tangerine)





