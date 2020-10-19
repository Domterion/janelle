import discord

from discord.ext import typed_commands

import config

from bot.bot import Janelle


class IamRoles(typed_commands.Cog[typed_commands.Context]):
    def __init__(self, bot: Janelle) -> None:
        self.bot = bot

    def cog_check(self, ctx: typed_commands.Context) -> bool:
        assert isinstance(ctx.author, discord.Member)
        return config.mod_role in (r.id for r in ctx.author.roles)

    @typed_commands.guild_only()
    @typed_commands.command()
    async def kick(
        self, ctx: typed_commands.Context, member: discord.Member, *, reason: str = ""
    ) -> None:
        """Kick a member from the server."""
        reason = f"{ctx.author} ({ctx.author.id}): {reason}"
        await member.kick(reason=reason)
        await ctx.send("Let's hope they learn a lesson. If not, fite me!~")

    @typed_commands.guild_only()
    @typed_commands.command()
    async def ban(
        self, ctx: typed_commands.Context, member: discord.Member, *, reason: str = ""
    ) -> None:
        """Ban a member from the server."""
        reason = f"{ctx.author} ({ctx.author.id}): {reason}"
        await member.ban(reason=reason)
        await ctx.send("¡Terminado! Espero que no regresen...")

    @typed_commands.guild_only()
    @typed_commands.command()
    async def softban(
        self, ctx: typed_commands.Context, member: discord.Member, *, reason: str = ""
    ) -> None:
        """Bans a member and unbans them immediately."""
        reason = f"[Softban] {ctx.author} ({ctx.author.id}): {reason}"
        await member.ban(reason=reason)
        await member.unban(reason=reason)
        await ctx.send("¡Éxito! I wouldn't want to see that hammer again...")

    @typed_commands.guild_only()
    @typed_commands.command()
    async def mute(
        self, ctx: typed_commands.Context, member: discord.Member, *, reason: str = ""
    ) -> None:
        """Mutes a member."""
        assert ctx.guild is not None
        reason = f"{ctx.author} ({ctx.author.id}): {reason}"
        role = discord.utils.get(ctx.guild.roles, id=config.mute_role)
        assert role is not None
        await member.add_roles(role, reason=reason)
        await ctx.send("It haz been done. Coke anyone?")

    @typed_commands.guild_only()
    @typed_commands.command()
    async def unmute(
        self, ctx: typed_commands.Context, member: discord.Member, *, reason: str = ""
    ) -> None:
        """Unmutes a member."""
        assert ctx.guild is not None
        reason = f"{ctx.author} ({ctx.author.id}): {reason}"
        role = discord.utils.get(ctx.guild.roles, id=config.mute_role)
        assert role is not None
        await member.remove_roles(role, reason=reason)
        await ctx.send(
            "Party in backyard? Oh, I suppose this is jail so better not :^)"
        )


def setup(bot: Janelle) -> None:
    bot.add_cog(IamRoles(bot))
