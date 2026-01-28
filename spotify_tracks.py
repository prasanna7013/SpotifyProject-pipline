import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector


sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='6146cfd679f14d34b031afc30f8227d3',
    client_secret='7015127f052547e0a191517fe4d8b8ab'
))

db_config={
    'host': 'localhost',
    'user':'root',
    'password':'Kanakam@1234',
    'database':'spotify_db'
}

connection =mysql.connector.connect(**db_config)
cursor=connection.cursor()

track_url='https://open.spotify.com/track/7ouMYWpwJ422jRcDASZB7P?si=1254567890abcdef'

track_id=re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

track =sp.track(track_id)

track_data={
    'name': track['name'],
    'album': track['album']['name'],
    'artist': track['artists'][0]['name'],
    'release_date': track['album']['release_date'],
    'duration_ms': track['duration_ms']/2,
    'popularity': track['popularity']
}


insert_query= """
INSERT INTO spotify_tracks(track_name,artist,album,popularity,duration_minutes)
VALUES(%s, %s, %s, %s, %s)
"""

cursor.execute(insert_query, (
    track_data['name'],
    track_data['artist'],
    track_data['album'],
    track_data['popularity'],
    track_data['duration_ms']
))

connection.commit()

print(f"Track '{track_data['name']}' by {track_data['artist']} inserted into the database.")

cursor.close()
connection.close()