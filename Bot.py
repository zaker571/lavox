import discord
import random
import os
from discord.ext import commands
client = commands.Bot("/")
@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.online,activity=discord.Game("Joy"))
        print("bot is ready.")

@client.event
async def on_member_join(member):
    print(f"{member} Joined The Server")

@client.event
async def on_member_remove(member):
    print(f"{member}Left The Server")
@client.command()
async def cmds(ctx):
    await ctx.send(".ping, .rolladice, .clear(amount needed!), .8Ball (Question), ")
@client.command()
async def ping(ctx):
    await ctx.send("PONG")
@client.command()
async def rolladice(ctx):
    await ctx.send(random.randrange(1,6,1))
@client.command()
async def clear(ctx,AMOUNT=5):
    await ctx.channel.purge(limit = AMOUNT + 1)
@client.command(aliases=["8Ball"])
async def _8ball(ctx,*,question):
    responses = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes - definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    await ctx.send(responses[random.randrange(0,20,1)])
@client.command()
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} have been kicked sucessfully")
@client.command()
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user} have been banned sucessfully")
@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user


client.run(os.environ["token"])