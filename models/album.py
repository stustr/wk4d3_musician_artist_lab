class Album: 
    def __init__(self, title, artist, genre, id = None) -> None:
        self.title = title
        self.genre = genre
        self.artist = artist
        self.id = id