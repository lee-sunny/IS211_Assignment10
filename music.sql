DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS songs;

CREATE TABLE artists(
    artist_id INTEGER NOT NULL PRIMARY KEY,
    artist_name TEXT
);

CREATE TABLE albums (
    album_id INTEGER NOT NULL PRIMARY KEY,
    album_name TEXT,
    artist_id INT
);

CREATE TABLE songs (
    song_id INTEGER NOT NULL PRIMARY KEY,
    song_name TEXT,
    track_number INT,
    track_length INT,
    album_id INT
);
