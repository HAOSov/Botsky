import requests
from bs4 import BeautifulSoup

# Constants for URLs
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"
LOG_FILE = "unfollows_log.txt"

def fetch_followers():
    """Fetches the current list of followers from the Bluesky profile page."""
    # URL of the Bluesky profile (replace YOUR_PROFILE_URL with actual URL)
    url = "YOUR_PROFILE_URL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        # Parse followers from HTML
        followers = parse_followers(response.text)
        return followers
    except requests.RequestException:
        raise ConnectionError("Failed to connect to Bluesky profile page.")

def parse_followers(html_content):
    """Parses the HTML content to extract the list of followers."""
    soup = BeautifulSoup(html_content, 'html.parser')
    followers = []
    # Extract follower nicknames and handles
    for follower_div in soup.find_all("div", class_="follower-class"):
        nick = follower_div.find("span", class_="nick-class").text.strip()
        handle = follower_div.find("span", class_="handle-class").text.strip()
        followers.append({"nick": nick, "handle": handle})
    return followers

def check_unfollowers(prev_followers, curr_followers):
    """Compares two lists of followers to find unfollowers."""
    unfollowers = [f for f in prev_followers if f not in curr_followers]
    return unfollowers

def log_event(event_text):
    """Logs an event to the log file."""
    with open(LOG_FILE, "a") as file:
        file.write(event_text + "\n")

def send_discord_notification(unfollower, unfollow_time):
    """Sends a notification to Discord via webhook."""
    message = {
        "content": f"User {unfollower['nick']} ({unfollower['handle']}) unfollowed at {unfollow_time}."
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=message)
        response.raise_for_status()
    except requests.RequestException as e:
        log_event(f"Failed to send Discord notification: {e}")
