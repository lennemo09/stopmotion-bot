import os
import discord
import time

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
COMMAND_ANIMATE = 'animate:'
COMMAND_REPEAT = 'repeat:'
REFRESH_RATE = 1
REPEAT_DEFAULT = 1

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')

@client.event
async def on_message(message):
    repeat = REPEAT_DEFAULT
    if message.author == client.user:
        return

    if  message.content.startswith(COMMAND_REPEAT):
        repeat = int(str(message.content[len(COMMAND_REPEAT)::]))
        print(f'Repeating {repeat} times.')

    if  message.content.startswith(COMMAND_ANIMATE):
        frames_string = str(message.content[len(COMMAND_ANIMATE)::])
        frames_list = frames_string.split('|')
        print(frames_list)

        channel_id = message.channel.id
        msg_id = None

        for _ in range(repeat):
            for frame in frames_list:
                print(frame)
                if msg_id == None:
                    payload = await message.channel.send(frame)
                    msg_id = payload
                else:
                    time.sleep(2)
                    await payload.edit(content=frame)
        repeat = REPEAT_DEFAULT

        return





client.run(TOKEN)
