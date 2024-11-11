from atproto import Client
from time import sleep
import traceback,datetime
from discord_webhook import DiscordWebhook
from reusable.string_functions import splash




def login_to_bluesky():
    client.login(BLUESKY_USERNAME, BLUESKY_PASSWORD)

def followers_list():
    follows = []
    try:
        did_response = client.com.atproto.identity.resolve_handle({'handle': BLUESKY_USERNAME})
        did = did_response['did']
        followers_response = client.get_followers(did)
        for i in followers_response.followers:
            handle = i.handle
            name = i.display_name
            if handle not in follows:
                follows.append([handle,name])
    except Exception as e:
        print(f"Error fetching followers: {e}")

    return follows

def send_to_discord(message):
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content=message)
    response = webhook.execute()
    return response



def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")

if __name__ == '__botsky__':
    splash('Bluesky Unfollow (Hater) Notification \nVersion 0.1 by HAOSov')
    sleep(1)

