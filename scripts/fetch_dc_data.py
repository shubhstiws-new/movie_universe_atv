import requests
import json
import os
import time

# TMDB API Configuration
API_KEY = "3ab424d92ea0058efd654775001c1c12"
BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

CONFIG = {
    "api_key": API_KEY,
    "data_dir": "BondUniverse/Data",
    "posters_dir": "BondUniverse/Data/posters"
}

# DC Content (focusing on main DCEU + key standalone films)
DC_CONTENT = {
    "Pre-DCEU Films": [
        {"title": "Superman", "year": 1978, "type": "movie"},
        {"title": "Batman", "year": 1989, "type": "movie"},
        {"title": "Batman Returns", "year": 1992, "type": "movie"},
        {"title": "Batman Forever", "year": 1995, "type": "movie"},
        {"title": "Batman & Robin", "year": 1997, "type": "movie"},
        {"title": "Superman Returns", "year": 2006, "type": "movie"},
        {"title": "Watchmen", "year": 2009, "type": "movie"},
        {"title": "Green Lantern", "year": 2011, "type": "movie"}
    ],
    "DCEU": [
        {"title": "Man of Steel", "year": 2013, "type": "movie"},
        {"title": "Batman v Superman: Dawn of Justice", "year": 2016, "type": "movie"},
        {"title": "Suicide Squad", "year": 2016, "type": "movie"},
        {"title": "Wonder Woman", "year": 2017, "type": "movie"},
        {"title": "Justice League", "year": 2017, "type": "movie"},
        {"title": "Aquaman", "year": 2018, "type": "movie"},
        {"title": "Shazam!", "year": 2019, "type": "movie"},
        {"title": "Birds of Prey", "year": 2020, "type": "movie"},
        {"title": "Wonder Woman 1984", "year": 2020, "type": "movie"},
        {"title": "The Suicide Squad", "year": 2021, "type": "movie"},
        {"title": "Black Adam", "year": 2022, "type": "movie"},
        {"title": "Shazam! Fury of the Gods", "year": 2023, "type": "movie"},
        {"title": "The Flash", "year": 2023, "type": "movie"},
        {"title": "Blue Beetle", "year": 2023, "type": "movie"},
        {"title": "Aquaman and the Lost Kingdom", "year": 2023, "type": "movie"}
    ],
    "Elseworlds": [
        {"title": "Joker", "year": 2019, "type": "movie"},
        {"title": "The Batman", "year": 2022, "type": "movie"}
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

def process_dc_content():
    all_content = []
    
    for era, items in DC_CONTENT.items():
        print(f"\n=== Processing {era} ===")
        
        for item in items:
            title = item["title"]
            year = item["year"]
            
            print(f"\nProcessing: {title} ({year})")
            
            search_result = search_movie(title, year)
            if search_result:
                details = get_movie_details(search_result["id"])
                if details:
                    poster_filename = f"{title.lower().replace(' ', '_').replace(':', '').replace('!', '').replace('&', 'and')}_{year}.jpg"
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
    print("DC UNIVERSE DATA PIPELINE")
    print("=" * 60)
    
    dc_content = process_dc_content()
    save_metadata(dc_content, "dc_metadata.json")
    
    print("\n" + "=" * 60)
    print(f"Pipeline Complete! Total Movies: {len(dc_content)}")
    print("=" * 60)
