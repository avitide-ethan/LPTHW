from sys import argv

script, filename = argv

print("Opening the file...\n")

target = open(filename, 'r')

read_target = target.read()
target.close()

print("""Going to erase {}.
Here's what it reads now: \n{}  \n \n
If you don't want that, hit CTRL-C. 
If you do want that hit, RETURN""".format(filename, read_target))

input("> ")


print("Truncating the file. Later homie!!")
write_target = open(filename, 'w')

line1, line2, line3 = input("\nline 1: "), input("\nline 2: "), input("\nline 3: ")

print(line1, line2, line3, sep="\n")

write_target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
