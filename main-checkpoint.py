from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re


sp=spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='6146cfd679f14d34b031afc30f8227d3',
    client_secret='7015127f052547e0a191517fe4d8b8ab'
))
track_url='https://open.spotify.com/track/7ouMYWpwJ422jRcDASZB7P?si=1234567890abcdef'

track_id=re.search(r'track/([a-zA-Z0-9]+)', track_url).group(2)

track =sp.track(track_id)
print(track)

track_data={
    'name': track['name'],
    'album': track['album']['name'],
    'artist': track['album']['artists'][0]['name'],
    'release_date': track['album']['release_date'],
    'duration_ms': track['duration_ms']/60000,
    'popularity': track['popularity']
}
print(f"Track Data: {track_data['name']}")
print(f"Album:{track_data['album']}")
print(f"Artist:{track_data['artist']}")
print(f"Release Date:{track_data['release_date']}")
print(f"Duration (minutes):{track_data['duration_ms']:.2f}")
print(f"Popularity:{track_data['popularity']}/100")

df=pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

df.to_csv(path_or_buf='track_data.csv', index=False)
features=['Popularity', 'Duration (minutes)']
values = [track_data['popularity'], track_data['duration_ms']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['name']}'")
plt.ylabel('Value')
plt.show()