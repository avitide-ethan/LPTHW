import sys
script, input_encoding, error, direction = sys.argv


def main(language_file, encoding, errors, direction):
    # define line as a line of the language_file
    line = language_file.readline()

    if line:
        # print that line
        if direction == 'forward':
            print_line(line, encoding, errors)
        if direction == 'backward':
            print_byte_to_line(line, encoding, errors)
        # return the language file back to the function to do it again ?
        return main(language_file, encoding, errors, direction)


# this does the encoding of each line from languagaes.txt
def print_line(line, encoding, errors):
    # strip away a "/n" from teh end of the line
    next_lang = line.strip()
    # take the language from languages.txt and encode into raw bytes
    # DBES: decode bytes, encode strings. how does this make sense? we just encoded "into bytes"
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # decode raw bytes back into string
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(cooked_string, "<====>", raw_bytes)
    # print("Next lang: \n{}".format(next_lang))


#
# main(languages, input_encoding, error)
#
# languages = open("languages.txt", encoding='utf-8')

def print_byte_to_line(line, encoding, errors):

    next_line = line.strip()

    string = next_line.encode(encoding, errors=errors)
    cooked_bytes = string.decode(encoding, errors=errors)
    print(string, "<-->", cooked_bytes)


languages = open("languages.txt", encoding='utf-8')

main(languages, input_encoding, error, direction)


# TODO: program that writes languages_bytes.txt from any languages.txt input file
