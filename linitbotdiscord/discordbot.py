# discord bot
# modules 
import os
import discord
import dotenv
import random
import wikipedia

dotenv.load_dotenv()
token = os.getenv("bot_token")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is now online")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!greeting"): # if it recieves this message
        await message.channel.send("Hello!") # reply with this

    if message.content.startswith("!roll"):
        roll = random.randint(1,6)
        await message.channel.send(f"you roll a {roll}!")

    if message.content.startswith("!search"):
     await message.channel.send("What do you want to search for?")
     search = await client.wait_for("message")
     result = wikipedia.summary(search.content)
     await message.channel.send(result)
     
    if message.content.startswith("!math"):
        await message.channel.send("ok, what is the first number?")
        num1 = await client.wait_for("message")
        await message.channel.send("ok, what is the second number?")
        num2 = await client.wait_for("message")
        answer = int(num1.content) + int(num2.content)
        await message.channel.send(f"the result is {answer}")


client.run(token)