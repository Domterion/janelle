from discord import Role, utils
from discord.ext.typed_commands import Context, RoleConverter, errors


class BetterRoleConverter(RoleConverter):
    async def convert(self, ctx: Context, argument: str) -> Role:
        try:
            return await super().convert(ctx, argument)
        except errors.RoleNotFound:
            if ctx.guild is not None:
                role = utils.find(
                    lambda r: r.name.lower() == argument.lower(),
                    ctx.guild.roles,
                )
            else:
                role = None
        if role is None:
            raise errors.RoleNotFound()
        return role
