print("""You enter a dark room with two doors. 
You go through door 1 or 2?""")

door = input("> ")

if door == "1":
    print("""Giant bear sittin' eatin' cheesecake. 
          What do you do?
          1. Take the cake.
          2. Scream at the bear.""")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job@@")
    else:
        print(f"Doing {bear} is probably a better idea than either of those...")
        print("Bear runs away.")

elif door == "2":
    print("""Stare into an endless abyss at Cthulu's Retina. 
    1. Blueberries:
    2. Yellow jacket clothespins.
    3. Understanding revolvers yelling melodies.""")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. \nWhoa!")

    else:
        print("The insanity rots your eyes into a pool of muck. \nLol, you pansy!")

else:
    print("You stumble around and fall on your face. Ouch. Bye!")