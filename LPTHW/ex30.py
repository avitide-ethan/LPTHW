people = 80
cars = 30
trucks = 50

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("Can't decide cars or not.")

if trucks>cars:
    print("Too many trucks doe.")
elif trucks<cars:
    print("Maybe take the trucks")
else:
    print("Still can't decide about trucks.")

if people > trucks:
    print("Aiiiight, let's take the trucks.")
else:
    print("Fuckit, let's stay home doe.")

if cars - trucks > people:
    print("Dude why are there so many vehicles")
elif cars + trucks > people:
    print("More vehicles than you need")
else:
    print("There seems to be a reasonable number of vehicles, I guess, ya know")