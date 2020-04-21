# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS 
        songplays (
            songplay_id SERIAL PRIMARY KEY,
            start_time TIMESTAMP,
            user_id INT,
            level VARCHAR,
            song_id VARCHAR,
            artist_id VARCHAR,
            session_id INT,
            location VARCHAR,
            user_agent VARCHAR
            )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS
        users ( 
            user_id PRIMARY KEY,
            first_name VARCHAR,
            last_name VARCHAR,
            gender VARCHAR,
            level VARCHAR
        )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS
        songs (
            song_id VARCHAR PRIMARY KEY,
            title VARCHAR,
            artist_id VARCHAR,
            year INT,
            duration NUMERIC
        )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS 
        artists (
            artist_id VARCHAR PRIMARY KEY,
            name VARCHAR,
            location VARCHAR,
            latitute NUMERIC,
            longitude NUMERIC
        )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS
        time (
            start_time TIMESTAMP PRIMARY KEY,
            hour INT,
            day INT,
            week INT,
            month INT,
            year INT,
            weekday INT
        )
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO 
        songplays (
            songplay_id,
            start_time,
            user_id,
            level,
            song_id,
            artist_id,
            session_id,
            location,
            user_agent
        )
        VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
    INSERT INTO
        users (
            user_id,
            first_name,
            last_name,
            gender,
            level
        )
        VALUES
            (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""
    INSERT INTO
        songs (
            song_id,
            title,
            artist_id,
            year,
            duration
        )
        VALUES
            (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
    INSERT INTO
        artists (
            artist_id,
            name,
            location,
            latitutde,
            longitude
        )
""")


time_table_insert = ("""
    INSERT INTO
        time (
            start_time,
            hour,
            day,
            week,
            month,
            year,
            weekday
        )
""")

# FIND SONGS

song_select = ("""
    SELECT
        *
    FROM
        songs
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]