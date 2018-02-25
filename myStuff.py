class Song(object):

    def __init__(self, lyrics, instruments):
        self.lyrics = lyrics
        self.instruments = instruments
        print("I'm initialized")

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def instrument_inventory(self):
        for instrument in self.instruments:
            print(instrument)

    def sing_me_with_instruments(self):
        self.instrument_inventory()
        self.sing_me_a_song()

# bulls_on_parade = Song(["Rally round the family,"
#                         "with pockets full of shells"],
#                        ["drums", "bass guitar",
#                         "electric guitar", "vocals"])
#
# happy_birthday = Song(["Happy birthday to you"
#                        "Trying not to get sued"
#                        "Stopping right dere"],
#                        ["Voices"])
# print("Singing now")
# bulls_on_parade.sing_me_a_song()
# print("Instruments as follows")
# bulls_on_parade.instrument_inventory()
#
# happy_birthday.sing_me_with_instruments()


def apple():
    print("I am APPPLEZZZ!!")


tangerine = "Living reflection of a dream"
