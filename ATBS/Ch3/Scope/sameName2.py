def spam():
    global eggs
    eggs = 'spam'


eggs = 'global'
spam()
print(eggs)

'''the eggs value is first defined as 'global' but then is redefined 
as 'spam' in the spam function. '''