DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    artist INT REFERENCES artists(id)
);

/* INSERT INTO artists (name)
VALUES ('Outkast');

INSERT INTO albums (title, genre)
VALUES ('Stankonia', 'Hip-hop'); */