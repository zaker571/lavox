import discord
from discord.ext import commands
import random
client = commands.Bot("£")
@client.event
async def on_ready():
    print("Bot IS Ready.")
@client.command()
async def sayhello(ctx):
    responses = ["Hi!","Hello, sunshine","Howdy, partner","Hey, howdy, hi!"]
    await ctx.send(responses[random.randrange(0,4)])
@client.command()
async def prefix(ctx):
    embed = discord.Embed(
        color=discord.Colour.gold(),
        title="Prefixes",
        description="Jbot-/, C-Bot - £"
    )
    
    embed.set_author(name="Author",icon_url= "https://uk.images.search.yahoo.com/search/images?p=MEME&fr=mcafee&imgurl=https%3A%2F%2Fwww.scoopify.org%2Fwp-content%2Fuploads%2F2019%2F06%2Fcheer-up-meme.jpg#id=1&iurl=https%3A%2F%2Fwww.scoopify.org%2Fwp-content%2Fuploads%2F2019%2F06%2Fcheer-up-meme.jpg&action=click")   
    embed.set_image(url="https://uk.images.search.yahoo.com/search/images?p=MEME&fr=mcafee&imgurl=https%3A%2F%2Fwww.scoopify.org%2Fwp-content%2Fuploads%2F2019%2F06%2Fcheer-up-meme.jpg#id=1&iurl=https%3A%2F%2Fwww.scoopify.org%2Fwp-content%2Fuploads%2F2019%2F06%2Fcheer-up-meme.jpg&action=click")
    embed.set_thumbnail(url="https://uk.images.search.yahoo.com/search/images?p=MEME&fr=mcafee&imgurl=https%3A%2F%2Fwww.scoopify.org%2Fwp-content%2Fuploads%2F2019%2F06%2Fcheer-up-meme.jpg#id=1&iurl=https%3A%2F%2Fwww.scoopify.org%2Fwp-content%2Fuploads%2F2019%2F06%2Fcheer-up-meme.jpg&action=click")
    embed.add_field(name="Jbot",value="/")
    embed.add_field(name="Me",value="£")
    await ctx.send(embed=embed)
@client.command()
async def Joke(ctx):
    jokes = ["Today at the bank, an old lady asked me to help check her balance. So I pushed her over.",
"I bought some shoes from a drug dealer. I don't know what he laced them with, but I've been tripping all day.",
"I told my girlfriend she drew her eyebrows too high. She seemed surprised.",
"My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.",
"I'm so good at sleeping. I can do it with my eyes closed.",
"I'm so good at sleeping. I can do it with my eyes closed."]
    await ctx.send( await ctx.send(jokes[random.randrange(0,5)]))
@client.command()    
async def suggest(ctx,suggestion):
    await print(suggestion)
client.run(config.token)