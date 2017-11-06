CREATE TABLE artists (
    id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE albums (
    id INTEGER PRIMARY KEY,
    name TEXT,
    artist INTEGER,
    FOREIGN KEY (artist) references artists (id)
);

CREATE TABLE songs (
    id INTEGER PRIMARY KEY,
    name TEXT,
    album INTEGER,
    track_no INTEGER,
    song_length INTEGER,
    FOREIGN KEY (album) references albums (id)
);