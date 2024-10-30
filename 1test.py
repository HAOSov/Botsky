import time
from datetime import datetime
from botsky_utils import fetch_followers, save_followers, log_event

# Define intervals in seconds
CHECK_INTERVAL = 3600  # 1 hour
RETRY_INTERVAL = 300   # 5 minutes

def main():
    # Initialize previous followers list as empty at the start
    previous_followers = fetch_followers()
    save_followers(previous_followers)
    log_event("Botsky started and saved initial followers list.")

    while True:
        try:
            # Fetch the current list of followers
            current_followers = fetch_followers()

            # Compare and save if there are changes
            if current_followers != previous_followers:
                save_followers(current_followers)
                log_event(f"Followers list updated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

            # Update previous followers list
            previous_followers = current_followers
            
            # Wait for the next check interval
            time.sleep(CHECK_INTERVAL)
        
        except ConnectionError:
            log_event("Connection error occurred, retrying in 5 minutes.")
            time.sleep(RETRY_INTERVAL)

if __name__ == "__main__":
    main()
