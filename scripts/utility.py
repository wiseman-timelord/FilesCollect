# utility.py

# Imports
import os, asyncio, aiohttp, requests, psutil, subprocess, time, random, json, random
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from torpy.http.adapter import TorHttpAdapter
from torpy import TorClient
from scripts.display import display_progress_bar, error_msgs



# Handle Errors
def handle_error(e):
    return error_msgs.get(type(e), "Error Occurred")

# Simplified Directory Creation
def create_dir_from_url(url):
    try:
        path = urlparse(url).path.lstrip('/').rsplit('.', 1)[0]
        return os.path.join(*path.split('/'))
    except Exception as e:
        print(f"Error parsing URL: {e}")
        return None

# Load Settings
def load_settings(config):
    try:
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            config.base_url_location_eia = settings.get("base_url_location_eia", "")
            config.file_type_search_fvb = settings.get("file_type_search_fvb", [])
            config.standard_mode_3nc = settings.get("standard_mode_3nc", True)
            config.max_concurrent_downloads_6d3 = settings.get("max_concurrent_downloads_6d3", 1)
            config.random_delay_r5y = settings.get("random_delay_r5y", "15")
            config.low_score_3hf = settings.get("low_score_3hf", float('inf'))
            config.high_score_6hd = settings.get("high_score_6hd", 0.0)
            config.TOR_PORT = settings.get("TOR_PORT", 9050)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading settings: {e}")
        print("Corrupted or Not Found! Using Default.")

# Save Settings
def save_settings(config):
    settings = {
        "base_url_location_eia": config.base_url_location_eia,
        "file_type_search_fvb": config.file_type_search_fvb,
        "standard_mode_3nc": config.standard_mode_3nc,
        "max_concurrent_downloads_6d3": config.max_concurrent_downloads_6d3,
        "random_delay_r5y": config.random_delay_r5y,
        "low_score_3hf": config.low_score_3hf,
        "high_score_6hd": config.high_score_6hd,
        "TOR_PORT": config.TOR_PORT
    }
    try:
        with open('settings.json', 'w') as f:
            json.dump(settings, f, indent=4)
    except Exception as e:
        print(f"Error saving settings: {e}")

def get_random_delay(random_delay_r5y):
    base_delay = 15
    max_additional_time = int(random_delay_r5y)
    total_delay = base_delay + random.randint(0, max_additional_time)
    return total_delay

