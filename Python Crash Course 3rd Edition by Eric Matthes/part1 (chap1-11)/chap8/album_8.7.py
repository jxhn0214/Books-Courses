def make_album(artist, album):
    album_info = {}
    album_info[artist.title()] = album.title()
    return album_info

album0 = make_album('frank ocean', 'blonde')
print(album0)

album1 = make_album('laufey', 'bewitched')
print(album1)

album2 = make_album('faye webster', 'atlanta millionaires club')
print(album2)

