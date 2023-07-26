import discord, requests
from discord.ext import commands
import googleapiclient.discovery

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

YOUTUBE_API_KEY = "YOUTUBE_API_KEY"
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    activity = discord.Game(name="ping for help")
    await bot.change_presence(activity=activity)

@bot.command(name='yt')
async def search(ctx, *, query):
    # Make a search request to the YouTube Data API
    request = youtube.search().list(
        q=query,
        part="snippet",
        maxResults=1
    )

    response = request.execute()

    if response["items"]:
        video_id = response["items"][0]["id"]["videoId"]
        video_link = f"https://www.youtube.com/watch?v={video_id}"
        await ctx.send(video_link)
    else:
        await ctx.send("No video found.")

SPOTIFY_CLIENT_ID = 'SPOTIFY_CLIENT_ID'
SPOTIFY_CLIENT_SECRET = 'SPOTIFY_CLIENT_SECRET'

def get_spotify_token():
    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(url, data=data, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
    return response.json()['access_token']
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # responds on ping
    if bot.user.mentioned_in(message):
        response = "type in :\n`!yt <search query>` to fetch links. \n`!joke` for dark jokes."
        await message.channel.send(response)

    await bot.process_commands(message)

    if message.content.startswith('!sp '):
            search_query = message.content[4:]
            access_token = get_spotify_token()
            headers = {
                'Authorization': f'Bearer {access_token}'
            }
            params = {
                'q': search_query,
                'type': 'track',
                'limit': 1
            }
            response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
            data = response.json()
            if 'tracks' in data and 'items' in data['tracks'] and len(data['tracks']['items']) > 0:
                track = data['tracks']['items'][0]
                song_name = track['name']
                spotify_url = track['external_urls']['spotify']
                await message.channel.send(f"Here's the Spotify link for '{song_name}': {spotify_url}")
            else:
                await message.channel.send("Sorry, couldn't find any matching song.")


# JOKE Command
@bot.command()
async def joke(ctx):
     # Fetch a random dark joke from the API
    response = requests.get('https://v2.jokeapi.dev/joke/Dark')
    data = response.json()

    # Check if the response contains a single or two-part joke
    if data['type'] == 'single':
        joke = data['joke']
    elif data['type'] == 'twopart':
        setup = data['setup']
        delivery = data['delivery']
        joke = f"{setup}\n{delivery}"
    else:
        joke = "Sorry, I couldn't fetch a dark joke."

    # Send the joke to the Discord channel
    await ctx.send(joke)

bot.run("DISCORD_BOT_TOKEN")
