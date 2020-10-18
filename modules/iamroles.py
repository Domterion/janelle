import discord

from discord.ext import typed_commands

import config

from bot.bot import Janelle


class IamRoles(typed_commands.Cog[typed_commands.Context]):
    def __init__(self, bot: Janelle) -> None:
        self.bot = bot

    @typed_commands.guild_only()
    @typed_commands.command()
    async def iamroles(self, ctx: typed_commands.Context) -> None:
        """List all self-assignable roles."""
        # Some mypy fixes for guild_only
        assert ctx.guild is not None
        text = "\n".join(
            [
                f"{discord.utils.get(ctx.guild.roles, id=id_)} (ID: {id_})"
                for id_ in config.roles
            ]
        )
        await ctx.send(text)

    @typed_commands.guild_only()
    @typed_commands.command()
    async def iam(self, ctx: typed_commands.Context, *, role: discord.Role) -> None:
        """Assign yourself a role."""
        if role.id not in config.roles:
            await ctx.send("Not today, cutie! That role is locked :(")
            return
        # Some mypy fixes for guild_only
        assert isinstance(ctx.author, discord.Member)
        await ctx.author.add_roles(role)
        await ctx.send("¡Claro!~")

    @typed_commands.guild_only()
    @typed_commands.command()
    async def iamnot(self, ctx: typed_commands.Context, *, role: discord.Role) -> None:
        """Remove a self-assignable role from yourself."""
        if role.id not in config.roles:
            await ctx.send("Not today, cutie! That role is locked :(")
            return
        # Some mypy fixes for guild_only
        assert isinstance(ctx.author, discord.Member)
        await ctx.author.remove_roles(role)
        await ctx.send("¡Claro!~")


def setup(bot: Janelle) -> None:
    bot.add_cog(IamRoles(bot))
