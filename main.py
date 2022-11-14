#spotipy or genius

def Get_lyrics(artist,song):
    return PyLyrics.getAlbums("Eminem")


print("Type the artist:")
artist = input()

print("Type the song name:")
song = input()

text = Get_lyrics(artist,song)
print(text)