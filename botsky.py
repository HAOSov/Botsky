import time
from datetime import datetime
from botsky_utils import fetch_followers, check_unfollowers, log_event, send_discord_notification

# Define intervals in seconds
CHECK_INTERVAL = 3600  # 1 hour
RETRY_INTERVAL = 300   # 5 minutes

def main():
    # Initialize previous followers list as empty at the start
    previous_followers = fetch_followers()
    log_event("Botsky started and fetched initial followers list.")

    while True:
        try:
            # Fetch current followers list
            current_followers = fetch_followers()
            
            # Check for unfollowers
            unfollowers = check_unfollowers(previous_followers, current_followers)
            if unfollowers:
                for unfollower in unfollowers:
                    # Get time of unfollowing
                    unfollow_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # Log and send notification
                    log_event(f"Unfollow detected: {unfollower['nick']} ({unfollower['handle']}) at {unfollow_time}")
                    send_discord_notification(unfollower, unfollow_time)
                    
            # Update previous followers list
            previous_followers = current_followers
            
            # Wait for the next check interval
            time.sleep(CHECK_INTERVAL)
        
        except ConnectionError:
            log_event("Connection error occurred, retrying in 5 minutes.")
            time.sleep(RETRY_INTERVAL)
        
if __name__ == "__main__":
    main()
