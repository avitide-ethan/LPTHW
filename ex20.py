from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")

current_file = open(input_file)

print("First print the whole thing\n")

print_all(current_file)

print("Now rewind")

rewind(current_file)

print("Print three lines")

current_line = input("Which line to start with? \n> ")

current_line = int(current_line)
for current_line in range(current_line, current_line + 3):
    print_a_line(current_line, current_file)
    current_line += 1
