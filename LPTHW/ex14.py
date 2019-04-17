from sys import argv
dib, user_name = argv
prompt = '> '

print("Hi {}, I'm the {} script.".format(user_name, dib))
print("Do you like me {}?".format(user_name))

likes = input(prompt)

print("Where do you live {}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""

Aiiighhhhht, so you said {} about liking me. You live in {}, 
not sure where dat is, annnnd you have a {} computer. Shweet.
""".format(likes, lives, computer))
