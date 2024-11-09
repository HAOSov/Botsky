from atproto import Client
from time import sleep
import traceback
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
                    print(f"Something wrong - can collect followers: {e}")

return follows

def send_to_discord(message):
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content=message)
    response = webhook.execute()
    return response
