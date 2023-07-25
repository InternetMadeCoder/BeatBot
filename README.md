# TubeBot
This is a simple Discord bot designed to fetch YouTube links based on user-provided search queries. It utilizes the YouTube Data API to perform a search and retrieve the most relevant video. When a user sends a command in the format `!yt <search query>`, the bot will search for videos matching the query and provide a link to the top result. If a video is found, the bot will respond with the YouTube link. If no video is found, it will inform the user accordingly. The bot enhances the Discord server by allowing users to easily access and share YouTube content within the community.

## How to setup
1. Clone the repository to the current directory.
   ```powershell
   https://github.com/InternetMadeCoder/TubeBot.git
   ```
   
2. Install the following packages.
   - discord.py
   ```powershell
   pip install discord.py
   ```
   - googleapiclient
   ```powershell
   pip install google-api-python-client
   ```
    - requests
   ```powershell
   pip install requests
   ```
   
3. Create a new file called `.env` and copy the format from `.env.example` (or you can just rename `.env.example`)

4. Update `.env` with your own credentials.

5. Start your bot

## Bot Invite Link
- [TubeBot](https://discord.com/oauth2/authorize?scope=bot&permissions=8&client_id=1120947722090975294)
