class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def play(self):
        for song in self.songs:
            song.play()


class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def play(self):
        print(f"Song now playing {self.title} by {self.artist}")

my_playlist = Playlist("My Playlist")
song1 = Song("I Love You", "Simple Plan")
song2 = Song("Wake Me Up", "Wham")

my_playlist.songs.append(song1)
my_playlist.songs.append(song2)

my_playlist.play()

'''
What we have here are two classes: a Playlist. I can see here that there's a has-a relationship. A playlist has a song or songs. But to determine whether or not song is a collaborator object, we have to see if Playlist delegates any of its responsibilities to the Song class. And we can see that that is the case within the play method in Playlist, because we iterate through each song in the instance variable songs, and then we call upon the play method that has been defined in the Song class. So this is also an example of composition as well, where we use other objects within the class to carry out its responsibility. 

'''