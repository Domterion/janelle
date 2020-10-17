import logging

from discord import AllowedMentions
from discord.ext.commands import errors
from discord.ext.typed_commands import Bot, Context, when_mentioned_or

import config


class Janelle(Bot[Context]):
    def __init__(self) -> None:
        allowed_mentions = AllowedMentions(roles=False, everyone=False, users=True)
        super().__init__(
            command_prefix=when_mentioned_or(config.prefix),
            fetch_offline_members=False,
            allowed_mentions=allowed_mentions,
        )
        for extension in config.extensions:
            self.load_extension(extension)

    async def on_ready(self) -> None:
        logging.info("Bot is ready")

    async def on_command_error(
        self, ctx: Context, error: Exception, bypass: bool = False
    ) -> None:
        if (
            hasattr(ctx.command, "on_error")
            or (ctx.command and hasattr(ctx.cog, f"_{ctx.command.cog_name}__error"))
            and not bypass
        ):
            # Do nothing if the command/cog has its own error handler
            return

        if isinstance(error, errors.RoleNotFound):
            await ctx.send(f'Could not find role "{error.argument}" :(')
