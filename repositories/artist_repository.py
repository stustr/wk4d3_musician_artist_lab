from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def select_all():
    
    artists = []
    
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    
    for row in results:
        artist = Artist(row['name'], row['id'])
        artists.append(artist)
    return artists

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        artist = artist(result['name'])
        return artist
    
def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)
    
def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)
    
def album_list(artist):
    albums_by_artist = []
    sql = "SELECT * FROM albums WHERE artist = %s"
    values = [artist.id]
    results = run_sql(sql, values)
    
    for row in results:
        album = Album(row['title'], row['artist'], row['genre'], row['id'])
        albums_by_artist.append(album.title)
        
    return f"\nAlbums by {artist.name}:\n {albums_by_artist}\n"