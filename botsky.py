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
