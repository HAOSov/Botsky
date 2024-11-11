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

delay = int(input('Enter refresh delay(seconds): '))
    sleep(2)
    with open('acc_data.txt','r',encoding='utf-8') as f:
        data = f.read().strip()
        data = data.split('\n')

with open('webhook_url.txt','r',encoding='utf-8') as f:
        hook_url = f.read().strip()

    BLUESKY_USERNAME = data[0]
    BLUESKY_PASSWORD = data[1]
    DISCORD_WEBHOOK_URL = hook_url

with open('action_logs.txt','r',encoding='utf-8') as f:
        action_logs = f.read()


    client = Client()

login_to_bluesky()
    print('Hello, Sensei. I Plana and I saw your video with Kokona. Calling KSPD')
    initial_follows = followers_list()
    print('KSPD scan your Momotalk')

while True:
        try:
            sleep(60)
            print('KSPD watching you...')
            current_follows = followers_list()
            unfollowed_users = []
            for init_f_ in initial_follows:
                if init_f_ not in current_follows:
                    unfollowed_users.append(init_f_)
                    
if unfollowed_users:
                unfollowed_message = f"You are unfollowed by {len(unfollowed_users)} possibly hater:"
                for user in unfollowed_users:
                    unfollowed_message += f"\n -{user[1]}(@{user[0]})"
                print(unfollowed_message)
                send_to_discord(unfollowed_message)
