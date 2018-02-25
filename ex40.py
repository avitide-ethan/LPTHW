class Song(object):
    def __init__(self, lyric_input):
        self.lyrics = lyric_input
        print("My lyrics were just input into the new instance of class SONG!")

    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)


happy_bday = Song(["Happy birthday to you,",
                   "I don't want to get sued,",
                   "So I'll stpo there."])

bulls_on_parade = Song(["They rally round da family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print(bulls_on_parade.lyrics[1])


for number in range(0, 3):
    print(happy_bday.lyrics[number])
