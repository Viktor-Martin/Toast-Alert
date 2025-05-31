import discord
import random
import asyncio
import RPi.GPIO as GPIO

server_chan_list = [
    {'server': 1100608571017797714, 'channel': 1100608572917809266},
    {'server': 639706647434100736, 'channel': 639706647434100739},
    {'server': 643844726419750922, 'channel': 643844726419750925}
]
async def check_toast_status(toast):
    state = 0
    while True:
        toast_state = GPIO.input(4)
        if(toast_state == 1):
            state = toast_state
        print(f"Toast state: {toast_state}, State: {state}")

        if toast_state != state and toast_state == 0:
            data = await find_user(toast)
            state = 0
            channel_id = 0
            for server in server_chan_list:
                if data[1].id == server['server']:
                    channel_id = server['channel']

            message_server = await toast.fetch_guild(data[1].id)
            message_channel = await message_server.fetch_channel(channel_id)
            await message_channel.send(f'<@{data[0].id}>, tell Viktor his toast is ready.')
        await asyncio.sleep(1)
async def find_user(toast:discord.Client):
    logserver = await toast.fetch_guild(1100608571017797714)
    logchannel = await logserver.fetch_channel(1152038437826863184)
    server_list = []
    for server in toast.guilds:
        server_list.append(server.id)

    server_count = len(server_list)
    selected_server = server_list[random.randrange(0, server_count)]
    server = await toast.fetch_guild(selected_server)

    server_members = server.fetch_members()
    user_list = []
    async for member in server_members:
        user_list.append(member.id)
    user_count = len(user_list)
    selected_user = user_list[random.randrange(0,user_count)]

    user = await toast.fetch_user(selected_user)
    await logchannel.send(f'Selected server: {server.name}\nSelected user: {user.name}')
    return [user, server]

async def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    class Toast(discord.Client):
        async def on_ready(toast):
            print(f'LOCKED IN\nChecking Toast Status...')
            asyncio.create_task(check_toast_status(toast))

    intents = discord.Intents.all()
    intents.message_content = True
    intents.members = True
    intents.guilds = True

    client = Toast(intents=intents)
    await client.start('Token here.')

if __name__ == "__main__":
    asyncio.run(main())