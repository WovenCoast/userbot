from configparser import ConfigParser

import spotipy
import spotipy.util as util

config_file = 'config/userbot.ini'

config = ConfigParser()
config.read(config_file)

username = config.get('spotify', 'username')
CLIENT_ID = config.get('spotify', 'client_id')
CLIENT_SECRET = config.get('spotify', 'client_secret')
redirect_uri = "http://localhost:8888/callback"
scope = 'user-read-currently-playing app-remote-control streaming'

print(username)
print(CLIENT_ID)
print(CLIENT_SECRET)

token = util.prompt_for_user_token(
    username=username,
    scope=scope,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=redirect_uri,
    cache_path='config/.cache-' + username
)

spotify = spotipy.Spotify(auth=token)
