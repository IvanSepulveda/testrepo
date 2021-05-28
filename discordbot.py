import discord


import random

from discord.ext import commands

import praw


reddit = praw.Reddit(
    client_id = '4YN54DcbV-2-sQ',
    client_secret = 'Ty0XXSEubMF8sKZrI8liM6yp4WIFaQ',
    username = 'PnkFalcon',
    password = 'fortnite',
    user_agent = 'V1'
)








client = commands.Bot(command_prefix = '.' )

@client.event
async def on_ready():
    print("bot is now online!")

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')
        
@client.command()
async def fact(ctx):
    sub = reddit.subreddit('facts')

    hot_python = sub.hot(limit=30)

    itemlist = []
    for submission in hot_python:
        if not submission.stickied:
            itemlist.append(submission.title)



 
    embed = discord.Embed(title="Fun Fact:", description= random.choice(itemlist), colour=discord.Colour.green())
    await ctx.send(embed = embed)


@client.command()
async def showerthought(ctx):
    sub = reddit.subreddit('showerthoughts')

    hot_python = sub.hot(limit=30)

    itemlist = []
    for submission in hot_python:
        if not submission.stickied:
            itemlist.append(submission.title)



 
    embed = discord.Embed(title="Heres a Shower Thought:", description= random.choice(itemlist), colour=discord.Colour.green())
    await ctx.send(embed = embed)



@client.command()
async def meme(ctx):
    sub = reddit.subreddit('memes')

    hot_python = sub.hot(limit=30)

    itemlist = []
    for submission in hot_python:
        if not submission.stickied:
            if "https://i." in submission.url:
                itemlist.append(submission.url)



 
    embed = discord.Embed(title=f"Meme", colour=discord.Colour.green())
    embed.set_image(url=random.choice(itemlist))
    await ctx.send(embed = embed)
    

@client.command()
async def cat(ctx):
    sub = reddit.subreddit('catpictures')

    hot_python = sub.hot(limit=30)

    itemlist = []
    for submission in hot_python:
        if not submission.stickied:
            if "https://i." in submission.url:
                itemlist.append(submission.url)



 
    embed = discord.Embed(title=f"Cat", colour=discord.Colour.green())
    media = random.choice(itemlist)
    embed.set_image(url=media)
    await ctx.send(embed = embed)


@client.command()
async def dog(ctx):
    sub = reddit.subreddit('dogpictures')

    hot_python = sub.hot(limit=30)

    itemlist = []
    for submission in hot_python:
        if not submission.stickied:
            if "https://i." in submission.url:
                itemlist.append(submission.url)



 
    embed = discord.Embed(title=f"Dog", colour=discord.Colour.green())
    embed.set_image(url=random.choice(itemlist))
    await ctx.send(embed = embed)








@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")


    for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    embed = discord.Embed(title="muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted")



@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

   await member.remove_roles(mutedRole)
   await member.send(f"you have been unmuted")
   embed = discord.Embed(title="unmute", description=f" unmuted-{member.mention}",colour=discord.Colour.light_gray())
   await ctx.send(embed=embed)



@client.command()
async def DMme(ctx):
    embed = discord.Embed(title="Sending", description=f"sending {ctx.author} a direct message!", colour=discord.Colour.green())
    await ctx.send(embed = embed)
    await ctx.author.send("I have dmed you")



@client.command()
async def commands(ctx):
    embed = discord.Embed(title="Commands:",description="this is the command list", colour=discord.Colour.orange())
    embed.add_field(name=".fact", value="gets you a fact", inline=False)
    embed.add_field(name=".showerthought", value="Gives you a thought that you would think of in the shower", inline=False)
    embed.add_field(name=".dog", value="gives you a picture of a dog", inline=False)
    embed.add_field(name=".cat", value="gives you a picture of a cat", inline=False)
    embed.add_field(name=".meme", value="gives you a meme", inline=False)
    embed.add_field(name=".userinfo", value="gives you info on a specific user", inline=False)
    embed.add_field(name=".mute", value="mutes people", inline=False)
    embed.add_field(name=".unmute", value="unmutes people", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def userinfo(ctx, member: discord.Member):
    embed = discord.Embed(title=f"User Info about {member.name}", colour=discord.Colour.light_gray())
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Nickname:", value=member.nick)
    embed.add_field(name="Status", value=member.raw_status)
    embed.add_field(name="Join Date:", value=member.created_at)
    await ctx.send(embed=embed)


client.run('ODM3MzgwNjM0MTI4MTU0Njg1.YIrtfA.uXfCP4TdHQVRgH4loQ2N9y6Xoko')