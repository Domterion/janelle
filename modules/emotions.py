import random

import discord

from discord.ext import typed_commands

import config

from bot.bot import Janelle


class Emotions(typed_commands.Cog[typed_commands.Context]):
    def __init__(self, bot: Janelle) -> None:
        self.bot = bot

    @typed_commands.guild_only()
    @typed_commands.command()
    async def poke(self, ctx: typed_commands.Context, member: discord.Member) -> None:
        """Poke a member."""
        embed = discord.Embed(
            title=f"{ctx.author.display_name} pokes {member.display_name}! Boop!",
            color=discord.Colour.from_hsv(random.random(), 1, 1),
        )
        embed.set_image(url=random.choice(config.pokes))
        await ctx.send(embed=embed)

    @typed_commands.guild_only()
    @typed_commands.command()
    async def hug(self, ctx: typed_commands.Context, member: discord.Member) -> None:
        """Hug a member."""
        embed = discord.Embed(
            title=f"{ctx.author.display_name} hugs {member.display_name}! Open your arms!",
            color=discord.Colour.from_hsv(random.random(), 1, 1),
        )
        embed.set_image(url=random.choice(config.hugs))
        await ctx.send(embed=embed)

    @typed_commands.guild_only()
    @typed_commands.command()
    async def cuddle(self, ctx: typed_commands.Context, member: discord.Member) -> None:
        """Cuddle a member."""
        embed = discord.Embed(
            title=f"{ctx.author.display_name} cuddles {member.display_name}! Don't jump on them!",
            color=discord.Colour.from_hsv(random.random(), 1, 1),
        )
        embed.set_image(url=random.choice(config.cuddles))
        await ctx.send(embed=embed)

    @typed_commands.guild_only()
    @typed_commands.command()
    async def kiss(self, ctx: typed_commands.Context, member: discord.Member) -> None:
        """Kiss a member."""
        embed = discord.Embed(
            title=f"{ctx.author.display_name} kisses {member.display_name}! Tongue please?",
            color=discord.Colour.from_hsv(random.random(), 1, 1),
        )
        embed.set_image(url=random.choice(config.kisses))
        await ctx.send(embed=embed)

    @typed_commands.guild_only()
    @typed_commands.command()
    async def pat(self, ctx: typed_commands.Context, member: discord.Member) -> None:
        """Pat a member."""
        embed = discord.Embed(
            title=f"{ctx.author.display_name} pats {member.display_name}! Cute~",
            color=discord.Colour.from_hsv(random.random(), 1, 1),
        )
        embed.set_image(url=random.choice(config.pats))
        await ctx.send(embed=embed)

    @typed_commands.guild_only()
    @typed_commands.command()
    async def dance(self, ctx: typed_commands.Context) -> None:
        """Dance in front of everyone else."""
        embed = discord.Embed(
            title=f"{ctx.author.display_name} dances! Turn up the music, everybody!",
            color=discord.Colour.from_hsv(random.random(), 1, 1),
        )
        embed.set_image(url=random.choice(config.dances))
        await ctx.send(embed=embed)


def setup(bot: Janelle) -> None:
    bot.add_cog(Emotions(bot))
