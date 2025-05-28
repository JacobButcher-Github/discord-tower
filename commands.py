from discord import Interaction
from discord.app_commands import CommandTree


def register_commands(tree: CommandTree):

    @tree.command(name="hello", description="Says hello")
    async def hello(interaction: Interaction):
        await interaction.response.send_message("Hi.", ephemeral=False)

    @tree.command(name="ephemeral-hello", description="says hello ephemerally")
    async def eph_hello(interaction: Interaction) -> None:
        await interaction.response.send_message("Hi. Ephemerally.", ephemeral=True)
