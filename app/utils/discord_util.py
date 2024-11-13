import discord
from discord.ext import commands
import asyncio

BOT_TOKEN = ""


async def send_message_to_channel(channel_id: int, message: str, bot_token: str):
    """
    Send a message to a specific Discord channel.

    :param channel_id: The ID of the channel to send the message to.
    :param message: The content of the message to send.
    :param bot_token: The Discord bot token for authentication.
    """
    # Add 'guilds' intent so the bot can access channel information
    intents = discord.Intents.default()
    intents.message_content = True
    intents.guilds = True  # Ensure guild-related events are accessible

    bot = commands.Bot(command_prefix='!', intents=intents)

    @bot.event
    async def on_ready():
        print(f"Bot is ready. Logged in as {bot.user.name}")
        channel = bot.get_channel(channel_id)

        if channel:
            await channel.send(message)
            print(f"Message sent to channel {channel.name} (ID: {channel_id})")
        else:
            print(f"Error: Channel with ID {channel_id} not found.")
        await bot.close()

    try:
        await bot.start(bot_token)
    except discord.errors.LoginFailure:
        print("Error: Invalid bot token. Please check your Discord bot token.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Ensure the asyncio.run works properly in your environment
if __name__ == "__main__":
    asyncio.run(send_message_to_channel(1293194363303759902, "Hello, Discord!",
                BOT_TOKEN))
