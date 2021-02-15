import discord
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

TOKEN = config.get('DEFAULT', 'BOT_TOKEN')
BOT_NAME = config.get('DEFAULT', 'BOT_NAME')

client = discord.Client()

@client.event
async def on_ready():
    print('on board!')

@client.event
async def reply(message):
    remove_author = message.content.replace("<*>", "")
    print(message.content)
    print(remove_author)
    # msg = f"{message.author.mention} {remove_author} を受け取りました。"
    # await message.channel.send(msg)

@client.event
async def on_message(message):
    if client.user in message.mentions:
        await reply(message)
    


client.run(TOKEN)