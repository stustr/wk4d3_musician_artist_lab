import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Outkast')
artist_repository.save(artist_1)

artist_2 = Artist('The Strokes')
artist_repository.save(artist_2)

artist_3 = Artist('Tame Impala')
artist_repository.save(artist_3)

artist_4 = Artist('Brockhampton')
artist_repository.save(artist_4)

album_1 = Album("Stankonia", artist_1, "Hip-hop")
album_repository.save(album_1)
album_2 = Album("ATLiens", artist_1, "Hip-hop")
album_repository.save(album_2)

album_3 = Album("Is this it", artist_2, "Rock")
album_repository.save(album_3)
album_4 = Album("The new abnormal", artist_2, "Rock")
album_repository.save(album_4)

album_5 = Album("Currents", artist_3, "Pop")
album_repository.save(album_5)
album_6 = Album("Lonerism", artist_3, "Rock")
album_repository.save(album_6)

album_7 = Album("Saturation 1", artist_4, "Hip-hop")
album_repository.save(album_7)
album_8 = Album("Saturation 2", artist_4, "Hip-hop")
album_repository.save(album_8)
album_9 = Album("Saturation 3", artist_4, "Hip-hop")
album_repository.save(album_9)

print(artist_repository.album_list(artist_3))

for album in album_repository.select_all():
    print(album.__dict__)

pdb.set_trace()