import re
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
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

file_path ="track_urls.txt"
with open(file_path, 'r') as f:
    track_urls = f.readlines()

for track_url in track_urls:
    track_url = track_url.strip()
    try:
        match = re.search(r'track/([a-zA-Z0-9]+)', track_url)
        if match:
            track_id = match.group(1)
            track = sp.track(track_id)
            track_data = {
                'name': track['name'],
                'album': track['album']['name'],
                'artist': track['album']['artists'][0]['name'],
                'release_date': track['album']['release_date'],
                'duration_minutes': track['duration_ms'] / 60000,
                'popularity': track['popularity']
            }
            
            insert_query = """
            INSERT INTO spotify_tracks(track_name, artist, album, popularity, duration_minutes)
            VALUES(%s, %s, %s, %s, %s)
            """
            
            cursor.execute(insert_query, (
                track_data['name'],
                track_data['artist'],
                track_data['album'],
                track_data['popularity'],
                track_data['duration_minutes']
            ))
            connection.commit()
            print(f"Inserted '{track_data['name']}' by {track_data['artist']}")
        else:
            print(f"Skipping invalid URL: {track_url}")
        
    except Exception as e:
        print(f"Error processing URL: {track_url}, Error: {e}")
        
    except Exception as e:
        print(f"Error processing URL :{track_urls},Error{e}")


cursor.close()
connection.close()

print("All traack have been processed and insert into the database.")