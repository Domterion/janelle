import logging

import discord

from discord.ext import typed_commands

import config

from bot.bot import Janelle


class Rules(typed_commands.Cog[typed_commands.Context]):
    def __init__(self, bot: Janelle) -> None:
        self.bot = bot

    @typed_commands.Cog.listener()
    async def on_raw_reaction_add(
        self,
        ev: discord.raw_models.RawReactionActionEvent,
    ) -> None:
        if (
            ev.message_id == config.rules_message_id
            and ev.emoji.id == config.rules_emoji_id
        ):
            await self.bot.http.add_role(  # type: ignore
                ev.guild_id, ev.user_id, config.member_role, reason="Rules"
            )
            logging.info("Gave a role due to rule accepting")


def setup(bot: Janelle) -> None:
    bot.add_cog(Rules(bot))
