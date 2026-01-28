# Spotify Project Pipeline

A Python-based data pipeline that fetches Spotify track information and stores it in a MySQL database.

## Features

- Fetch track metadata from Spotify API
- Parse Spotify URLs to extract track IDs
- Store track data in MySQL database
- Extract information: track name, artist, album, popularity, duration

## Prerequisites

- Python 3.7+
- MySQL Server
- Spotify API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/prasanna7013/SpotifyProject-pipline.git
cd SpotifyProject-pipline
```

2. Create a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root (copy from `.env.example`):
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=spotify_db
```

2. Set up your MySQL database:
```sql
CREATE DATABASE spotify_db;
USE spotify_db;

CREATE TABLE spotify_tracks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    track_name VARCHAR(255),
    artist VARCHAR(255),
    album VARCHAR(255),
    popularity INT,
    duration_minutes FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Usage

1. Create a `track_urls.txt` file with Spotify track URLs (one per line):
```
https://open.spotify.com/track/...
https://open.spotify.com/track/...
```

2. Run the script:
```bash
python spotify_mysql_url.py
```

## Project Structure

```
├── spotify_mysql_url.py      # Main pipeline script
├── spotify_tracks.py         # Track processing utilities
├── main-checkpoint.py        # Checkpoint/backup version
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── track_urls.txt           # Input: Spotify track URLs
└── track_data.csv           # Output: Track data
```

## API References

- [Spotify API Documentation](https://developer.spotify.com/documentation/web-api)
- [Spotipy Library](https://spotipy.readthedocs.io/)

## License

MIT License

## Author

Prasanna - @prasanna7013
