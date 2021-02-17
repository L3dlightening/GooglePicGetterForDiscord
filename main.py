import discord
import configparser
import re
import src.get_pic_from_google as gpfg

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
    remove_author_from_message = re.sub("\<.+?\>", "", message.content)
    pic = gpfg.get_image_link(remove_author_from_message)
    await message.channel.send(pic)


@client.event
async def on_message(message):
    if client.user in message.mentions:
        await reply(message)

client.run(TOKEN)