import discord
from discord.ext import commands

class ServerBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

        self.server = None

    async def on_ready(self):
        print(f'Logged in as {self.user}')

        # Create a new server
        self.server = await self.create_guild(name='My Server')

        # Add yourself to the server
        await self.add_user(self.user, self.server)

        # Set the server as the bot's default server
        self.default_guild = self.server

        # Send the server's link to the user
        await self.send_message(self.user, f'The server's link is {self.server.invite_url}')

        # Set the server to always be online
        await self.server.set_auto_archive_duration(0)

    async def on_message(self, message):
        # If the message is from the bot itself, ignore it
        if message.author == self.user:
            return

        # If the message contains the command `!status`, print the server's status
        if message.content == '!status':
            print(f'Server status: {self.server.status}')

    async def on_command(self, ctx):
        # If the command is not recognized, print an error message
        if ctx.command is None:
            print(f'Unknown command: {ctx.message.content}')
            return

        # Otherwise, execute the command
        await self.dispatch(ctx.command)

if __name__ == '__main__':
    bot = ServerBot()
    bot.run('6394505280:AAHVKo6X0R-BvDp6VkOSwHyEUZjJmuO1uhE')
