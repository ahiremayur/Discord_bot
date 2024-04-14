import os
import discord
from discord.ext import commands
import requests
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)

# Define intents
intents = discord.Intents.default()  # This enables the default intents like guilds and messages
intents.messages = True  # Explicitly enable the messages intent if you need to handle messages

# Initialize the bot with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def weather(ctx, *, city: str):
    # Replace 'Your_API_Key' with your actual OpenWeatherMap API key
    api_key = 'b0d30ecea802631c3780560195da1a05'
   
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get('weather'):
        weather = response['weather'][0]['description']
        temperature = response['main']['temp']
        reply = f"It's currently {weather} in {city}, with a temperature of {temperature}°C. "
        reply += "Perfect weather for a cup of tea and a good book, don’t you think?"
    else:
        reply = "I couldn't find that city. Are you sure it’s not a hidden paradise?"
    await ctx.send(reply)

# Run the bot
bot.run(os.getenv('DISCORD_TOKEN')) 
