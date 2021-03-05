song = {
    "artist": "Biggie Smalls",
    "genre": "Hip-Hop/Rap",
    "release year": "1994",
    "isAlive" : "False",
    "title" : "Juicy"
}

for key in song:
    print("{0:s}: \"{1:s}\"".format(key.capitalize(), song[key]))

def guess(key, val):
    return key in song and song[key] == val

print("Is the title of this song \"Juicy\"?: {}".format(
    guess("title", "Juicy")))

