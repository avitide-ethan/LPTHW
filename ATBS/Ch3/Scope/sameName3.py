def spam():
    global eggs
    eggs = 'spam'  # this is the global


def bacon():
    eggs = 'bacon'


def ham():
    print(eggs)  # global one


eggs = 42
spam()
print(eggs)

