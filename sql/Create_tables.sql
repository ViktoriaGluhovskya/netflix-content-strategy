CREATE TABLE shows (
    id INT AUTO_INCREMENT PRIMARY KEY,
    show_id VARCHAR(10) UNIQUE,
    type VARCHAR(20),
    title TEXT,
    date_added DATE,
    release_year INT,
    rating VARCHAR(10),
    duration VARCHAR(20),
    description TEXT
);

CREATE TABLE countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE show_countries (
    show_id INT,
    country_id INT,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (country_id) REFERENCES countries(id),
    PRIMARY KEY (show_id, country_id)
);

CREATE TABLE actors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE show_actors (
    show_id INT,
    actor_id INT,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (actor_id) REFERENCES actors(id),
    PRIMARY KEY (show_id, actor_id)
);

CREATE TABLE genres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE show_genres (
    show_id INT,
    genre_id INT,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id),
    PRIMARY KEY (show_id, genre_id)
);

CREATE TABLE directors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) UNIQUE
);

CREATE TABLE show_directors (
    show_id INT,
    director_id INT,
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (director_id) REFERENCES directors(id),
    PRIMARY KEY (show_id, director_id)
);