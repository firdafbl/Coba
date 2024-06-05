class Penyanyi:
    def __init__(self, artist):
        self.artist = artist
        print("artist:", self.artist)

    def sing_a_song(self):
        print("sing a song")

class Maliq:
    def __init__(self, artist):
        self.artist = artist
        print("artist:", self.artist)

    def sing_a_song(self):
        print("Kita Bikin Romantis")


si_penyanyi = Penyanyi("Artist Penyanyi")
si_penyanyi.sing_a_song()
si_Maliq = Maliq("Maliq")
si_Maliq.sing_a_song()
        