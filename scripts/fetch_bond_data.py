import requests
import json
import os
import time

# Configuration
import os

API_READ_ACCESS_TOKEN = os.environ.get("TMDB_READ_TOKEN", "YOUR_READ_TOKEN")
BASE_URL = "https://api.themoviedb.org/3"
OUTPUT_DIR = "BondUniverse/Data"
POSTERS_DIR = os.path.join(OUTPUT_DIR, "posters")

HEADERS = {
    "Authorization": f"Bearer {API_READ_ACCESS_TOKEN}",
    "accept": "application/json"
}

# Daniel Craig's Bond Movies
# All James Bond Movies by Era (Newest to Oldest)
MOVIES_TO_FETCH = [
    # Daniel Craig (2006–2021)
    {"title": "No Time to Die", "year": 2021},
    {"title": "Spectre", "year": 2015},
    {"title": "Skyfall", "year": 2012},
    {"title": "Quantum of Solace", "year": 2008},
    {"title": "Casino Royale", "year": 2006},

    # Pierce Brosnan (1995–2002)
    {"title": "Die Another Day", "year": 2002},
    {"title": "The World Is Not Enough", "year": 1999},
    {"title": "Tomorrow Never Dies", "year": 1997},
    {"title": "GoldenEye", "year": 1995},

    # Timothy Dalton (1987–1989)
    {"title": "Licence to Kill", "year": 1989},
    {"title": "The Living Daylights", "year": 1987},

    # Roger Moore (1973–1985)
    {"title": "A View to a Kill", "year": 1985},
    {"title": "Octopussy", "year": 1983},
    {"title": "For Your Eyes Only", "year": 1981},
    {"title": "Moonraker", "year": 1979},
    {"title": "The Spy Who Loved Me", "year": 1977},
    {"title": "The Man with the Golden Gun", "year": 1974},
    {"title": "Live and Let Die", "year": 1973},

    # George Lazenby (1969)
    {"title": "On Her Majesty's Secret Service", "year": 1969},

    # Sean Connery (1962–1967, 1971)
    {"title": "Diamonds Are Forever", "year": 1971},
    {"title": "You Only Live Twice", "year": 1967},
    {"title": "Thunderball", "year": 1965},
    {"title": "Goldfinger", "year": 1964},
    {"title": "From Russia with Love", "year": 1963},
    {"title": "Dr. No", "year": 1962}
]

def get_config():
    """Fetch API configuration to get base image URL."""
    url = f"{BASE_URL}/configuration"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def search_movie(title, year):
    """Search for a movie by title and year."""
    url = f"{BASE_URL}/search/movie"
    params = {
        "query": title,
        "year": year,
        "include_adult": "false",
        "language": "en-US",
        "page": 1
    }
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    results = response.json().get("results", [])
    if results:
        return results[0] # Return the first match
    return None

def get_movie_details(movie_id):
    """Get full movie details."""
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"language": "en-US"}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()

def download_image(file_path, url):
    """Download an image from a URL."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        print(f"Downloaded: {file_path}")
    else:
        print(f"Failed to download image: {url}")

def main():
    print("Starting TMDB Data Pipeline...")
    
    # Ensure directories exist
    os.makedirs(POSTERS_DIR, exist_ok=True)
    
    # 1. Get Configuration
    try:
        config = get_config()
        base_image_url = config['images']['secure_base_url']
        poster_size = "original" # Use highest resolution
        print(f"API Configured. Image Base URL: {base_image_url}")
    except Exception as e:
        print(f"Error fetching config: {e}")
        return

    all_movies_data = []

    # 2. Fetch Data for each movie
    for movie_info in MOVIES_TO_FETCH:
        title = movie_info['title']
        year = movie_info['year']
        print(f"\nProcessing: {title} ({year})")
        
        try:
            # Search
            search_result = search_movie(title, year)
            if not search_result:
                print(f"Movie not found: {title}")
                continue
            
            movie_id = search_result['id']
            print(f"Found ID: {movie_id}")
            
            # Details
            details = get_movie_details(movie_id)
            all_movies_data.append(details)
            
            # Download Poster
            poster_path = details.get('poster_path')
            if poster_path:
                image_url = f"{base_image_url}{poster_size}{poster_path}"
                filename = f"{title.replace(' ', '_').lower()}_{year}.jpg"
                save_path = os.path.join(POSTERS_DIR, filename)
                download_image(save_path, image_url)
                
                # Update local path in data
                details['local_poster_path'] = f"Data/posters/{filename}"
            else:
                print("No poster path found.")
                
            time.sleep(0.2) # Be nice to the API
            
        except Exception as e:
            print(f"Error processing {title}: {e}")

    # 3. Save Metadata
    metadata_path = os.path.join(OUTPUT_DIR, "bond_metadata.json")
    with open(metadata_path, 'w') as f:
        json.dump(all_movies_data, f, indent=4)
    print(f"\nMetadata saved to: {metadata_path}")
    print("Pipeline Complete!")

if __name__ == "__main__":
    main()
