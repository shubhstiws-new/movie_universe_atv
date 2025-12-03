import requests
import json
import os
import time
from pathlib import Path

# TMDB API Configuration
import os

API_KEY = os.environ.get("TMDB_API_KEY", "YOUR_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Configuration
CONFIG = {
    "api_key": API_KEY,
    "data_dir": "Data",
    "posters_dir": "Data/posters"
}

# Marvel Cinematic Universe Content
MARVEL_CONTENT = {
    "Phase One": [
        {"title": "Iron Man", "year": 2008, "type": "movie"},
        {"title": "The Incredible Hulk", "year": 2008, "type": "movie"},
        {"title": "Iron Man 2", "year": 2010, "type": "movie"},
        {"title": "Thor", "year": 2011, "type": "movie"},
        {"title": "Captain America: The First Avenger", "year": 2011, "type": "movie"},
        {"title": "The Avengers", "year": 2012, "type": "movie"}
    ],
    "Phase Two": [
        {"title": "Iron Man 3", "year": 2013, "type": "movie"},
        {"title": "Thor: The Dark World", "year": 2013, "type": "movie"},
        {"title": "Captain America: The Winter Soldier", "year": 2014, "type": "movie"},
        {"title": "Guardians of the Galaxy", "year": 2014, "type": "movie"},
        {"title": "Avengers: Age of Ultron", "year": 2015, "type": "movie"},
        {"title": "Ant-Man", "year": 2015, "type": "movie"}
    ],
    "Phase Three": [
        {"title": "Captain America: Civil War", "year": 2016, "type": "movie"},
        {"title": "Doctor Strange", "year": 2016, "type": "movie"},
        {"title": "Guardians of the Galaxy Vol. 2", "year": 2017, "type": "movie"},
        {"title": "Spider-Man: Homecoming", "year": 2017, "type": "movie"},
        {"title": "Thor: Ragnarok", "year": 2017, "type": "movie"},
        {"title": "Black Panther", "year": 2018, "type": "movie"},
        {"title": "Avengers: Infinity War", "year": 2018, "type": "movie"},
        {"title": "Ant-Man and the Wasp", "year": 2018, "type": "movie"},
        {"title": "Captain Marvel", "year": 2019, "type": "movie"},
        {"title": "Avengers: Endgame", "year": 2019, "type": "movie"},
        {"title": "Spider-Man: Far From Home", "year": 2019, "type": "movie"}
    ],
    "Phase Four": [
        {"title": "Black Widow", "year": 2021, "type": "movie"},
        {"title": "Shang-Chi and the Legend of the Ten Rings", "year": 2021, "type": "movie"},
        {"title": "Eternals", "year": 2021, "type": "movie"},
        {"title": "Spider-Man: No Way Home", "year": 2021, "type": "movie"},
        {"title": "Doctor Strange in the Multiverse of Madness", "year": 2022, "type": "movie"},
        {"title": "Thor: Love and Thunder", "year": 2022, "type": "movie"},
        {"title": "Black Panther: Wakanda Forever", "year": 2022, "type": "movie"},
        {"title": "WandaVision", "year": 2021, "type": "tv"},
        {"title": "The Falcon and the Winter Soldier", "year": 2021, "type": "tv"},
        {"title": "Loki", "year": 2021, "type": "tv"},
        {"title": "Hawkeye", "year": 2021, "type": "tv"},
        {"title": "Moon Knight", "year": 2022, "type": "tv"},
        {"title": "Ms. Marvel", "year": 2022, "type": "tv"},
        {"title": "She-Hulk: Attorney at Law", "year": 2022, "type": "tv"}
    ],
    "Phase Five": [
        {"title": "Ant-Man and the Wasp: Quantumania", "year": 2023, "type": "movie"},
        {"title": "Guardians of the Galaxy Vol. 3", "year": 2023, "type": "movie"},
        {"title": "The Marvels", "year": 2023, "type": "movie"},
        {"title": "Deadpool & Wolverine", "year": 2024, "type": "movie"},
        {"title": "Secret Invasion", "year": 2023, "type": "tv"},
        {"title": "Echo", "year": 2024, "type": "tv"},
        {"title": "Agatha All Along", "year": 2024, "type": "tv"}
    ],
    "Phase Six": [
        {"title": "The Fantastic Four: First Steps", "year": 2025, "type": "movie"}
    ]
}

def get_config():
    """Load configuration"""
    os.makedirs(CONFIG["data_dir"], exist_ok=True)
    os.makedirs(CONFIG["posters_dir"], exist_ok=True)
    return CONFIG

def search_movie(title, year):
    """Search for a movie by title and year"""
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": CONFIG["api_key"],
        "query": title,
        "year": year
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
    return None

def search_tv(title, year):
    """Search for a TV show by title and year"""
    url = f"{BASE_URL}/search/tv"
    params = {
        "api_key": CONFIG["api_key"],
        "query": title,
        "first_air_date_year": year
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
    return None

def get_movie_details(movie_id):
    """Get detailed movie information"""
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": CONFIG["api_key"]}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def get_tv_details(tv_id):
    """Get detailed TV show information"""
    url = f"{BASE_URL}/tv/{tv_id}"
    params = {"api_key": CONFIG["api_key"]}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def download_poster(poster_path, filename):
    """Download poster image"""
    if not poster_path:
        return None
    
    url = f"{IMAGE_BASE_URL}{poster_path}"
    filepath = os.path.join(CONFIG["posters_dir"], filename)
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, 'wb') as f:
            f.write(response.content)
        return f"Data/posters/{filename}"
    return None

def process_marvel_content():
    """Process all Marvel content"""
    all_content = []
    
    for phase, items in MARVEL_CONTENT.items():
        print(f"\n=== Processing {phase} ===")
        
        for item in items:
            title = item["title"]
            year = item["year"]
            content_type = item["type"]
            
            print(f"\nProcessing: {title} ({year}) [{content_type}]")
            
            # Search for content
            if content_type == "movie":
                search_result = search_movie(title, year)
                if search_result:
                    details = get_movie_details(search_result["id"])
                    if details:
                        # Download poster
                        poster_filename = f"{title.lower().replace(' ', '_').replace(':', '').replace('&', 'and')}_{year}.jpg"
                        local_poster_path = download_poster(details.get("poster_path"), poster_filename)
                        
                        content_data = {
                            "id": details["id"],
                            "title": details["title"],
                            "overview": details["overview"],
                            "release_date": details["release_date"],
                            "vote_average": details["vote_average"],
                            "runtime": details.get("runtime", 0),
                            "local_poster_path": local_poster_path,
                            "type": "movie",
                            "phase": phase
                        }
                        all_content.append(content_data)
                        print(f"✓ Found movie ID: {details['id']}")
                        if local_poster_path:
                            print(f"✓ Downloaded poster: {local_poster_path}")
            
            elif content_type == "tv":
                search_result = search_tv(title, year)
                if search_result:
                    details = get_tv_details(search_result["id"])
                    if details:
                        # Download poster
                        poster_filename = f"{title.lower().replace(' ', '_').replace(':', '').replace('&', 'and')}_{year}.jpg"
                        local_poster_path = download_poster(details.get("poster_path"), poster_filename)
                        
                        content_data = {
                            "id": details["id"],
                            "title": details["name"],
                            "overview": details["overview"],
                            "first_air_date": details.get("first_air_date", f"{year}-01-01"),
                            "vote_average": details["vote_average"],
                            "number_of_seasons": details.get("number_of_seasons"),
                            "number_of_episodes": details.get("number_of_episodes"),
                            "local_poster_path": local_poster_path,
                            "type": "tv",
                            "phase": phase
                        }
                        all_content.append(content_data)
                        print(f"✓ Found TV show ID: {details['id']}")
                        if local_poster_path:
                            print(f"✓ Downloaded poster: {local_poster_path}")
            
            # Rate limiting
            time.sleep(0.25)
    
    return all_content

def save_metadata(content, filename):
    """Save metadata to JSON file"""
    filepath = os.path.join(CONFIG["data_dir"], filename)
    with open(filepath, 'w') as f:
        json.dump(content, f, indent=2)
    print(f"\n✓ Metadata saved to: {filepath}")

if __name__ == "__main__":
    get_config()
    
    print("=" * 60)
    print("MARVEL CINEMATIC UNIVERSE DATA PIPELINE")
    print("=" * 60)
    
    marvel_content = process_marvel_content()
    
    # Separate movies and TV shows
    movies = [c for c in marvel_content if c["type"] == "movie"]
    tv_shows = [c for c in marvel_content if c["type"] == "tv"]
    
    # Save to separate files
    if movies:
        save_metadata(movies, "marvel_movies.json")
    if tv_shows:
        save_metadata(tv_shows, "marvel_tv.json")
    
    # Also save combined
    save_metadata(marvel_content, "marvel_metadata.json")
    
    print("\n" + "=" * 60)
    print(f"Pipeline Complete!")
    print(f"Total Movies: {len(movies)}")
    print(f"Total TV Shows: {len(tv_shows)}")
    print("=" * 60)
