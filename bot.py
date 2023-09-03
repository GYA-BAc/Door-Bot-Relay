

# load bot key
with open(".env") as file:
    KEY = file.readline().strip()

import discord



bot = discord.Bot(command_prefix="!", intents = discord.Intents.all(), help_command=help_command)


@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'door':
        pass


bot.run(KEY)