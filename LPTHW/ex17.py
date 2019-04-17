from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))

indata = open(from_file).read()

print("Input file is {} bytes, does output exist?".format(len(indata)), exists(to_file))


out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()

fo_out = open(to_file, 'r')
print("Your new file reads: \n{}".format(fo_out.read()))
fo_out.close()
