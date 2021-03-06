from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.utils = self.bot.get_cog('Utils')

    @commands.group(name='help', invoke_without_command=True)
    @commands.guild_only()
    async def help_command(self, ctx: commands.Context) -> None:
        prefix = await self.utils.get_prefix(ctx.guild.id)

        embed = discord.Embed(title='Commands')
        if await ctx.bot.is_owner(ctx.author):
            embed.add_field(name='Admin Commands', value=f'`{prefix}help admin`', inline=False)

        embed.add_field(name='Device Commands', value=f'`{prefix}help device`', inline=False)
        embed.add_field(name='TSS Commands', value=f'`{prefix}help tss`', inline=False)
        embed.add_field(name='Miscellaneous Commands', value=f'`{prefix}help misc`', inline=False)
        embed.add_field(name="If this is your first time using AutoTSS, run this for more information", value=f'`{prefix}info`', inline=False)

        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url_as(static_format='png'))
        await ctx.send(embed=embed)

    @help_command.command(name='devices', aliases=('device',))
    @commands.guild_only()
    async def device_commands(self, ctx: commands.Context) -> None:
        prefix = await self.utils.get_prefix(ctx.guild.id)

        embed = discord.Embed(title='Device Commands')
        embed.add_field(name='Add a device', value=f'`{prefix}devices add`', inline=False)
        embed.add_field(name='Remove a device', value=f'`{prefix}devices remove`', inline=False)
        embed.add_field(name='List your devices', value=f'`{prefix}devices list`', inline=False)
        if await ctx.bot.is_owner(ctx.author):
            embed.add_field(name='Transfer devices to new user', value=f'`{prefix}devices transfer <old user> <new user>`', inline=False)

        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url_as(static_format='png'))
        await ctx.send(embed=embed)

    @help_command.command(name='tss')
    @commands.guild_only()
    async def tss_commands(self, ctx: commands.Context) -> None:
        prefix = await self.utils.get_prefix(ctx.guild.id)

        embed = discord.Embed(title='TSS Commands')
        embed.add_field(name='Save blobs for all of your devices', value=f'`{prefix}tss save`', inline=False)
        embed.add_field(name='List all blobs saved for your devices', value=f'`{prefix}tss list`', inline=False)
        embed.add_field(name='Download all blobs saved for your devices', value=f'`{prefix}tss download`', inline=False)
        if await ctx.bot.is_owner(ctx.author):
            embed.add_field(name='Download all blobs saved for all devices', value=f'`{prefix}tss downloadall`', inline=False)
            embed.add_field(name='Save blobs for all devices', value=f'`{prefix}tss saveall`', inline=False)

        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url_as(static_format='png'))
        await ctx.send(embed=embed)

    @help_command.command(name='misc')
    @commands.guild_only()
    async def misc_commands(self, ctx: commands.Context) -> None:
        prefix = await self.utils.get_prefix(ctx.guild.id)

        embed = discord.Embed(title='Miscellaneous Commands')
        embed.add_field(name='Change the command prefix for AutoTSS', value=f'`{prefix}prefix <prefix>`', inline=False)
        embed.add_field(name='Get the invite for this bot', value=f'`{prefix}invite`', inline=False)
        embed.add_field(name='See the latency of this bot', value=f'`{prefix}ping`', inline=False)
        embed.add_field(name='Information about AutoTSS', value=f'`{prefix}info`', inline=False)

        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url_as(static_format='png'))
        await ctx.send(embed=embed)

    @help_command.command(name='admin')
    @commands.guild_only()
    @commands.is_owner()
    async def admin_commands(self, ctx: commands.Context) -> None:
        prefix = await self.utils.get_prefix(ctx.guild.id)

        embed = discord.Embed(title='Admin Commands')
        embed.add_field(name='See module subcommands', value=f'`{prefix}module`', inline=False)

        embed.set_footer(text=ctx.author.display_name, icon_url=ctx.author.avatar_url_as(static_format='png'))
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
