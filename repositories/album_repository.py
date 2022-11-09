from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def select_all():
    
    albums = []
    
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    
    for row in results:
        album = Album(row['title'], row['artist'], row['genre'], row['id'])
        albums.append(album)
    return albums

def save(album):
    sql = "INSERT INTO albums (title, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        album = Album(result['title'], result['genre'], result['artist'], result['id'])
        return album
    
def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)
    
def update(album):
    sql = "UPDATE albums SET (title, genre, artist) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist]
    run_sql(sql, values)