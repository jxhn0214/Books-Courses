def make_album(artist, album):
    album_info = {}
    album_info[artist.title()] = album.title()
    return album_info

while True: 
    print("\nenter an artist's name and their album")
    print("please press the letter 'q' at any time to exit the program\n")

    artist = input("Artist: ")
    if artist.lower() == 'q':
        break 
    album = input("Album: ")
    if album.lower() == 'q': 
        break

    album = make_album(artist, album)
    print(f"\n{album}")

