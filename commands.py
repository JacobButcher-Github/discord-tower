import discord
from discord import Interaction
from discord.app_commands import CommandTree
from discord.ui import Button, View

from tower_bot import TowerClient


def register_commands(client: TowerClient, tree: CommandTree):

    @tree.command(name="button-hello", description="Ephemeral message with buttons")
    async def button_hello(interaction: Interaction):
        class MyView(View):
            @discord.ui.button(label="👍", style=discord.ButtonStyle.green)
            async def thumbs_up(self, interaction_btn: Interaction, button: Button):
                await interaction_btn.response.send_message(
                    "You clicked 👍.", ephemeral=True
                )

            @discord.ui.button(label="👎", style=discord.ButtonStyle.red)
            async def thumbs_down(self, interaction_btn: Interaction, button: Button):
                await interaction_btn.response.send_message(
                    "You clicked 👎.", ephemeral=True
                )

        await interaction.response.send_message(
            "Click a button.", view=MyView(), ephemeral=True
        )
