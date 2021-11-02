import discord
import datetime
from discord.ext import commands
import asyncio
import math
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option



client = commands.Bot(command_prefix='-')
client.remove_command('help')
slash = SlashCommand(client, sync_commands=True)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Looking For Holiays To Count On | /help"))
    print('Logged on as Countdown Bot')


@slash.slash(
    name="help",
    description="Displays Help Page",
    guild_ids=[874711189584764978]
    
    )
async def Help(ctx:SlashContext):

        # PAGE 1
        page_1 = discord.Embed(
            title="Chirstmas Commands!",
            description="Help for Christmas commands.",
            colour=discord.Colour.blue()
        )
        fields=[
            ("days", "Christmas Countdown", False),
            
        ]
        page_1.set_footer(
            text="Page 1 of 2 Made By Dark.#3143"
        )
        for name, value, inline in fields:
            page_1.add_field(
                name=name,
                value=value,
                inline=inline
            )

        # PAGE 2
        page_2 = discord.Embed(
            title="Easter",
            description="Help for Easter commands.",
            colour=discord.Colour.red()
        )
        fields=[
            ("Eday", "Easter Countdown", False),
            
        ]
        page_2.set_footer(
            text="Page 2 of 2 Made By Dark.#3143"
        )
        for name, value, inline in fields:
            page_2.add_field(
                name=name,
                value=value,
                inline=inline
            )

        

        # pagination stuff
        message = await ctx.send(embed=page_1)
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        await message.add_reaction("❌")
        pages = 5
        current_page = 1

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️", "❌"]

        while True:
            try:
                reaction, user = await ctx.bot.wait_for("reaction_add", timeout=60, check=check)

                if str(reaction.emoji) == "▶️" and current_page != pages:
                    current_page += 1

                    if current_page == 2:
                        await message.edit(embed=page_2)
                        await message.remove_reaction(reaction, user)
                    
                   
                        
                if str(reaction.emoji) == "◀️" and current_page > 1:
                    current_page -= 1
                    
                    if current_page == 1:
                        await message.edit(embed=page_1)
                        await message.remove_reaction(reaction, user)

                    elif current_page == 2:
                        await message.edit(embed=page_2)
                        await message.remove_reaction(reaction, user)
                    
                  

                if str(reaction.emoji) == "❌":
                    await message.delete()
                    break

                else:
                    await message.remove_reaction(reaction, user)
                    
            except asyncio.TimeoutError:
                await message.delete()
                break    

@slash.slash(
    name="Cdays",
    description="Shows How Long Till Christmas Day",
    guild_ids=[874711189584764978]
    
    )
async def days(ctx:SlashContext):
    delta = datetime.datetime(2021, 12, 25) - datetime.datetime.now()
    days = delta.days
    days_text = "days"
    if days == 1:
        days_text = "day"
    hours = math.floor(delta.seconds / 3600)
    minutes = math.ceil(delta.seconds / 60) - (hours * 60)
    minutes_text = "minutes"
    if minutes == 1:
        minutes_text = "minute"
    embed = discord.Embed(title="How Long Till Christmas?", description=f":christmas_tree:", color=0x00ff00)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/874711189584764981/904724425411272764/IMG_6255.jpg")
    embed.add_field(name=f"Until Christmas there are: **{days}** {days_text} ,**{hours}** hours ,**{minutes}** {minutes_text}", value="** **", inline=False)
    await ctx.send(embed=embed)
    print(f"{ctx.message.author} wants to know how many days are left until Christmas")

@slash.slash(
    name="Eday",
    description="Shows How Long Till Easter",
    guild_ids=[874711189584764978]
    
    )
async def Edays(ctx:SlashContext):
    delta = datetime.datetime(2022, 4, 17) - datetime.datetime.now()
    days = delta.days
    days_text = "days"
    if days == 1:
        days_text = "day"
    hours = math.floor(delta.seconds / 3600)
    minutes = math.ceil(delta.seconds / 60) - (hours * 60)
    minutes_text = "minutes"
    if minutes == 1:
        minutes_text = "minute"
    embed = discord.Embed(title="How Long Till Easter", description=f"** **", color=0x00ff00) 
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/874711189584764981/905051686152851497/IMG_6288.jpg") 
    embed.add_field(name=f"Until Easter there are: **{days}** {days_text} ,**{hours}** hours ,**{minutes}** {minutes_text}", value="** **", inline=False)
    await ctx.send(embed=embed)
    print(f"{ctx.message.author} wants to know how many days are left until Easter")

@slash.slash(
    name="Hday",
    description="Shows How Long Till Halloween",
    guild_ids=[874711189584764978]
    
    )
async def Hdays(ctx:SlashContext):
    delta = datetime.datetime(2022, 10, 31) - datetime.datetime.now()
    days = delta.days
    days_text = "days"
    if days == 1:
        days_text = "day"
    hours = math.floor(delta.seconds / 3600)
    minutes = math.ceil(delta.seconds / 60) - (hours * 60)
    minutes_text = "minutes"
    if minutes == 1:
        minutes_text = "minute"
    embed = discord.Embed(title="How Long Till Halloween", description=f"** **", color=0x00ff00)  
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/874711189584764981/905053931443486780/IMG_3753.jpg") 
    embed.add_field(name=f"Until Halloween there are: **{days}** {days_text} ,**{hours}** hours ,**{minutes}** {minutes_text}", value="** **", inline=False)
    await ctx.send(embed=embed)
    print(f"{ctx.message.author} wants to know how many days are left until Halloween")


@slash.slash(
    name="Fday",
    description="Shows How Long Till Father's Day",
    guild_ids=[874711189584764978]
    
    )
async def Fdays(ctx:SlashContext):
    delta = datetime.datetime(2022, 6, 19) - datetime.datetime.now()
    days = delta.days
    days_text = "days"
    if days == 1:
        days_text = "day"
    hours = math.floor(delta.seconds / 3600)
    minutes = math.ceil(delta.seconds / 60) - (hours * 60)
    minutes_text = "minutes"
    if minutes == 1:
        minutes_text = "minute"
    embed = discord.Embed(title="How Long Till Fathers Days", description=f"** **", color=0x00ff00)  
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/874711189584764981/905054383463600188/IMG_3754.jpg") 
    embed.add_field(name=f"Until Fathers Day there are: **{days}** {days_text} ,**{hours}** hours ,**{minutes}** {minutes_text}", value="** **", inline=False)
    await ctx.send(embed=embed)
    print(f"{ctx.message.author} wants to know how many days are left until Fathers Day")

@slash.slash(
    name="Mday",
    description="Shows How Long Till Mothers Days",
    guild_ids=[874711189584764978]
    
    )
async def Mdays(ctx:SlashContext):
    delta = datetime.datetime(2022, 3, 27) - datetime.datetime.now()
    days = delta.days
    days_text = "days"
    if days == 1:
        days_text = "day"
    hours = math.floor(delta.seconds / 3600)
    minutes = math.ceil(delta.seconds / 60) - (hours * 60)
    minutes_text = "minutes"
    if minutes == 1:
        minutes_text = "minute"
    embed = discord.Embed(title="How Long Till Mothers Day", description=f"** **", color=0x00ff00) 
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/874711189584764981/905055639187902495/IMG_3762.webp") 
    embed.add_field(name=f"Until Mothers Day there are: **{days}** {days_text} ,**{hours}** hours ,**{minutes}** {minutes_text}", value="** **", inline=False)
    await ctx.send(embed=embed)
    print(f"{ctx.message.author} wants to know how many days are left until Mothers Day")






@slash.slash(
    name="ping",
    description="Shows Bot Latency",
    guild_ids=[874711189584764978]
    
    )
async def _ping(ctx:SlashContext): 
    await ctx.send(f"Pong! {client.latency*1000}ms")

@slash.slash(
    name="test",
    description="Test message",
    guild_ids=[874711189584764978]
)
async def _test(ctx:SlashContext):
    await ctx.send("Hi Im A Test Response")


client.run('OTA0NzIwMDY5NDQyMDExMTk4.YX_oOQ.SB5d4tBz4pTSNfT1S1_VzuZBdow')
