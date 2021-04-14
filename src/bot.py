import os
import discord
import time

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
COMMAND = 'animate:'
REFRESH_RATE = 1

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if  message.content.startswith(COMMAND):
        frames_string = str(message.content[len(COMMAND)::])
        frames_list = frames_string.split('|')
        print(frames_list)

        channel_id = message.channel.id
        msg_id = None

        for frame in frames_list:
            print(frame)
            if msg_id == None:
                payload = await message.channel.send(frame)
                msg_id = payload
            else:
                time.sleep(2)
                await payload.edit(content=frame)

        return





client.run(TOKEN)
