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

# LOTR Content (focusing on Peter Jackson trilogy + Hobbit trilogy)
LOTR_CONTENT = {
    "Third Age": [
        # The Hobbit Trilogy
        {"title": "The Hobbit: An Unexpected Journey", "year": 2012, "type": "movie"},
        {"title": "The Hobbit: The Desolation of Smaug", "year": 2013, "type": "movie"},
        {"title": "The Hobbit: The Battle of the Five Armies", "year": 2014, "type": "movie"},
        # The Lord of the Rings Trilogy
        {"title": "The Lord of the Rings: The Fellowship of the Ring", "year": 2001, "type": "movie"},
        {"title": "The Lord of the Rings: The Two Towers", "year": 2002, "type": "movie"},
        {"title": "The Lord of the Rings: The Return of the King", "year": 2003, "type": "movie"}
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

def process_lotr_content():
    all_content = []
    
    for age, items in LOTR_CONTENT.items():
        print(f"\n=== Processing {age} ===")
        
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
                        "age": age
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
    print("LORD OF THE RINGS DATA PIPELINE")
    print("=" * 60)
    
    lotr_content = process_lotr_content()
    save_metadata(lotr_content, "lotr_metadata.json")
    
    print("\n" + "=" * 60)
    print(f"Pipeline Complete! Total Movies: {len(lotr_content)}")
    print("=" * 60)
