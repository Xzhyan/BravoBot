import discord
from discord import app_commands



class ErrorHandler():
    async def on_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "Você não tem permissão para usar esse comando",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "Ocorreu um error",
            ephemeral=True
        )


