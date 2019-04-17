from sys import exit

def input_number():
    while True:
        try:
            choice = int(input("> "))
        except ValueError:
            print("That ain't no number bru.")
            continue
        else:
            return choice

def gold_room():
    print("This room is full of gold. How much you gon' take? Enter a number")

    how_much = input_number()

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""There's a bear here.
It has a bunch of honey. 
Fat bear is in front of another door. 
How are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input("""1. Take honey
2. Taunt bear
3. Open door
> """)
        if choice.lower() == "take honey":
            dead("The bear looks at you then slaps your face off. ZZZzzzamn! Ow!")
        elif choice.lower() == "taunt bear" and not bear_moved:
            print("""The bear has moved from the door.
You can go through it now.""")
            bear_moved = True
        elif choice.lower() == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means!")

def cthulhu_room():
    print("""Here, you see the great EVIL Cthulhu.
He, it, whatever stares at you and you go insaaaane.
Do you flee for your life, or eat your head?""")

    choice = input("> ")

    if "flee" in choice.lower():
        start()
    elif "head" in choice.lower():
        dead("Well that was tasty!!!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("""You are in a dark room. 
There's a door to your right and left. 
Which one do you take?""")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice =="right":
        cthulhu_room()
    else:
        dead("YOu suck at typing and stumble around the room until you starve.")


start()