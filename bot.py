import discord

# load bot key
from env import KEY

# not needed
try:
    from env import ROLE
except Exception:
    ROLE = None



intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents = intents)


def update_counter():
    with open("tmp", "w") as file:
        file.write(f"{bot.ping_count}")


# count how many times door has been pinged
bot.ping_count = 0
update_counter()


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(message.content)

    if "door" in message.content.lower() or ROLE in message.content.lower():
        # await message.channel.send("testing")

        bot.ping_count += 1
        update_counter()


if __name__ == "__main__": 
    bot.run(KEY)