import requests
import json
import os
import time

# TMDB API Configuration
import os

API_KEY = os.environ.get("TMDB_API_KEY", "YOUR_API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

CONFIG = {
    "api_key": API_KEY,
    "data_dir": "BondUniverse/Data",
    "posters_dir": "BondUniverse/Data/posters"
}

# Star Wars Canon Content
STAR_WARS_CONTENT = {
    "Fall of the Jedi": [
        {"title": "Star Wars: Episode I - The Phantom Menace", "year": 1999, "type": "movie"},
        {"title": "Star Wars: Episode II - Attack of the Clones", "year": 2002, "type": "movie"},
        {"title": "Star Wars: Episode III - Revenge of the Sith", "year": 2005, "type": "movie"},
        {"title": "Star Wars: The Clone Wars", "year": 2008, "type": "movie"}
    ],
    "Reign of the Empire": [
        {"title": "Rogue One: A Star Wars Story", "year": 2016, "type": "movie"},
        {"title": "Solo: A Star Wars Story", "year": 2018, "type": "movie"}
    ],
    "Age of Rebellion": [
        {"title": "Star Wars", "year": 1977, "type": "movie"},  # A New Hope
        {"title": "Star Wars: Episode V - The Empire Strikes Back", "year": 1980, "type": "movie"},
        {"title": "Star Wars: Episode VI - Return of the Jedi", "year": 1983, "type": "movie"}
    ],
    "New Republic": [
        {"title": "Star Wars: The Force Awakens", "year": 2015, "type": "movie"},
        {"title": "Star Wars: The Last Jedi", "year": 2017, "type": "movie"},
        {"title": "Star Wars: The Rise of Skywalker", "year": 2019, "type": "movie"}
    ]
}

def get_config():
    os.makedirs(CONFIG["data_dir"], exist_ok=True)
    os.makedirs(CONFIG["posters_dir"], exist_ok=True)
    return CONFIG

def search_movie(title, year):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": CONFIG["api_key"], "query": title, "year": year}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        if results:
            return results[0]
    return None

def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": CONFIG["api_key"]}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

def download_poster(poster_path, filename):
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

def process_star_wars_content():
    all_content = []
    
    for era, items in STAR_WARS_CONTENT.items():
        print(f"\n=== Processing {era} ===")
        
        for item in items:
            title = item["title"]
            year = item["year"]
            
            print(f"\nProcessing: {title} ({year})")
            
            search_result = search_movie(title, year)
            if search_result:
                details = get_movie_details(search_result["id"])
                if details:
                    poster_filename = f"{title.lower().replace(' ', '_').replace(':', '').replace('-', '')}_{year}.jpg"
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
                        "era": era
                    }
                    all_content.append(content_data)
                    print(f"✓ Found movie ID: {details['id']}")
                    if local_poster_path:
                        print(f"✓ Downloaded poster: {local_poster_path}")
            
            time.sleep(0.25)
    
    return all_content

def save_metadata(content, filename):
    filepath = os.path.join(CONFIG["data_dir"], filename)
    with open(filepath, 'w') as f:
        json.dump(content, f, indent=2)
    print(f"\n✓ Metadata saved to: {filepath}")

if __name__ == "__main__":
    get_config()
    
    print("=" * 60)
    print("STAR WARS DATA PIPELINE")
    print("=" * 60)
    
    star_wars_content = process_star_wars_content()
    save_metadata(star_wars_content, "starwars_metadata.json")
    
    print("\n" + "=" * 60)
    print(f"Pipeline Complete! Total Movies: {len(star_wars_content)}")
    print("=" * 60)
