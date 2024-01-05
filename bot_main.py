import asyncio
import time
import praw
import os
import random

from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

load_dotenv()
channel_id = *******************
vc_1 = *******************
AFK_vc = *******************
user = '*******************'
member_backup = *******************

TOKEN="*******************"
REDDIT_ID="*******************"
REDDIT_SECRET_ID="-*******************"
REDDIT_USER="*******************"
REDDIT_PASS="*******************"

bot = commands.Bot(case_insensitive=True, command_prefix="bot ")
channel = bot.get_channel(channel_id)
DM = bot.get_channel(*******************)

os.chdir("D:\Misc_Apps\Discord Bot")

reddit = praw.Reddit(client_id = REDDIT_ID,
                     client_secret = REDDIT_SECRET_ID,
                     user_agent = "I am a bot",
                     username =REDDIT_USER, password = REDDIT_PASS)

#PING COMMAND
@bot.command(
	help="Ghost pings specified user in code 10 times.",
	brief="Ghost pings 10 times."
)

async def ping(ctx, member: discord.User=None):
    x = 0
    if member:
        while x <= 1000:
            await ctx.send(f"<@!{member.id}> DRINK WATER", delete_after=0.1)
            x = x + 1
    else:
        while x <= 1000:
            await ctx.send(f"<@!{member_backup}> DRINK WATER", delete_after=0.1)
            x = x + 1


#JOIN COMMAND
@bot.command(
    help="Joins call with special surprise. Need to be in voice channel.",
    brief="Joins call.",
    pass_context=True,
)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    user = ctx.message.author.id
    if not channel:
        await ctx.send(f"Thanks for giving me perms to spam you <@!{user}>")
        return
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source='helloVoice.mp3'))
    await asyncio.sleep(3)
    await voice.disconnect()

#BAN COMMAND
@bot.command(
    help="Bans User.",
    brief="Bans User.",
    pass_context=True,
)
@commands.has_role("Bot Admin")
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f'BYE BYE <@!{member.id}>')
    await member.kick(reason=None)
    time.sleep(1)
    await member.send(" Join back: https://discord.gg/*******************")
    await ctx.send(f'User {member} has been kicked')

#BAN COMMAND
@bot.command(
    help="Dms User.",
    brief="Dms User.",
    pass_context=True,
)

async def dm(ctx, member: discord.User, *, content=None):
    channel = await member.create_dm()
    # if ctx.message.attachments[0]:
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get(my_url) as resp:
    #             if resp.status != 200:
    #                 return await channel.send('Could not download file...')
    #             data = io.BytesIO(await resp.read())
    #             await channel.send(file=discord.File(data, 'cool_image.png'))
    #     await channel.send(url=ctx.message.attachments)
    if len(content) > 1:
        await channel.send(f"{content}")
    else:
        await channel.send("Join back: https://discord.gg/*******************")



#BAN COMMAND
@bot.command(
    help="Friends User once mentioned.",
    brief="Friends User.",
    pass_context=True,
)

async def friend(ctx, member: discord.Member, *, reason=None):
    user = member.id
    await user.send_friend_request()


#DISCONNECT COMMAND
@bot.command(
    help="Disconnect from Vc.",
    brief="Kick anyone.",
    pass_context=True,)

async def dip(ctx):
    channel = ctx.message.author.voice.channel
    user = ctx.message.author.id
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send(f"Thanks for giving me perms to spam you <@!{user}>")
        return


#RELPY COMMAND
@bot.command(
	help="Replys whatever Krish wants it to.",
	brief="Sends a predefined message."
)

async def speak(ctx):
    await ctx.channel.send("Hello newcomer.")

#JUGGLE COMMAND
@bot.command(
	help="Juggles someone at LITERAL light speed.",
	brief="Juggles mentioned user."
)

async def juggle(ctx,  member: discord.Member=None):
    vc = bot.get_channel(vc_1)
    vc2 = bot.get_channel(AFK_vc)
    if not member:
        victim = ctx.message.author
    else:
        victim = member
    await victim.move_to(vc2, reason=None)
    await victim.move_to(vc, reason=None)
    await victim.move_to(vc2, reason=None)
    await victim.move_to(vc, reason=None)
    await victim.move_to(vc2, reason=None)

#NICKNAME COMMAND
@bot.command(help="Changes mentioned member's nickname.",
             brief="Changes nickname.",
             pass_context=True,)

async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member} ')


#KICK COMMAND
@bot.command(
    help="Kick anyone from the server who has role below Bot Admin.",
    brief="Kick anyone.",
    pass_context=True,)

async def kick(ctx, member: discord.Member, *, reason=None):
    user = ctx.message.author
    await ctx.send(f'BYE BYE NURD')
    await user.kick(reason=None)
    time.sleep(1)
    await user.send(" Join back: https://discord.gg/*******************")
    await ctx.send(f'User {user} has been kicked')


#ROULETTE COMMAND
responses = ["click", "click", "click", "click", "click", "BANG"]
@bot.command(
    help="You have a 1/6 chance of getting kicked from the server.",
    brief="Play roulette.",
    pass_context=True,)

async def roulette(ctx):
    random_response = random.choice(responses)
    player = ctx.message.author
    player_id = ctx.message.author.id
    if random_response == "BANG":
        await ctx.send("I am sorry")
        await player.kick(reason=None)
        await player.send(" Join back loser: https://discord.gg/*******************")
    elif player == *******************:
        await ctx.send("I am sorry")
        await player.kick(reason=None)
        await player.send(" Join back loser: https://discord.gg/*******************")
    else:
        await ctx.send(f"SAFETY has been granted to <@!{player_id}>.")

@bot.command(
    help="Plays Riding Round in a Rover - Unkown P.",
    brief="Plays favorite song.",
    pass_context=True,
)

async def rover(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You need to ride into a vc")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    source = FFmpegPCMAudio('Riding around in a rover.mp3')
    player = voice.play(source)
    print (player)
    while not player:
        await asyncio.sleep(1)
    await voice.disconnect()

@bot.command(
    help="Disconnect Voice Channel.",
    brief="Disconnect Voice Channel.",
    pass_context=True,
)
async def disconnect(ctx):
    vc = ctx.voice_client
    if vc:
        await vc.disconnect(force=True)
        await ctx.send("Later")
    else:
        await ctx.send("I'm not in a channel")

def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()

@bot.command(
    help="Fully restarts bot from source.",
    brief="Stops bot.",
    pass_context=True,
)
async def stop(ctx):
    try:
        await bot.close()
    except:
        pass
    finally:
        os.system("python main.py")

@bot.command(
    help="Send a high-resolution picture.",
    brief="Send a high-resolution picture.",
    pass_context=True,
)
async def yish(ctx):
    await ctx.send(file=discord.File('*******************.gif'))


async def roll_barrel_animation(ctx, outcome):
    if outcome == True:
        embedVar = discord.Embed(title='Good Luck', color=0x00ff00)
        embedVar.set_image(url = "https://i.ibb.co/mHY6Qz8/small-safe.gif")
        await ctx.send(embed=embedVar)
        time.sleep(1)
    if outcome == False:
        embedVar = discord.Embed(title='Good Luck', color=0x00ff00)
        embedVar.set_image(url = "https://i.ibb.co/X3ppHFZ/small-safe.gif")
        await ctx.send(embed=embedVar)
        time.sleep(1)


#ROULETTE DUEL COMMAND
responses = ["click", "click", "click", "click", "click", "BANG"]
players = ["a", "b"]
@bot.command(
    help="You have a 1/6 chance of getting kicked from the server.",
    brief="Play roulette.",
    pass_context=True,)

async def duel(ctx, member: discord.Member):
    p1_turn = True
    p2_turn = True
    reply = False
    p1_streak = 0
    p2_streak = 0
    player1 = ctx.message.author
    print(member)
    player2 = member
    random_response = random.choice(responses)
    random_player = random.choice(players)
    while p1_turn:
        if random_response == "BANG":
            await roll_barrel_animation(ctx, outcome=False)
            await ctx.send(f"<@!{player1.id}>'s been bopped, streak of {p1_streak} is over.")
            break
        else:
            await roll_barrel_animation(ctx, outcome=True)
            await ctx.send(f"SAFETY has been granted to <@!{player1.id}>.")
        random_response = random.choice(responses)
        p1_streak = p1_streak + 1

    await ctx.send(f"Rolling for <@!{player2.id}>.")
    while p2_turn:
        if random_response == "BANG":
            await roll_barrel_animation(ctx, outcome=False)
            await ctx.send(f"<@!{player2.id}>'s been bopped, streak of {p2_streak} is over.")
            break
        # elif player1 == 551550033128849411:
        #     await ctx.send(f"SAFETY has been granted to <@!{player2.id}>.")
        else:
            await roll_barrel_animation(ctx, outcome=True)
            await ctx.send(f"SAFETY has been granted to <@!{player2.id}>.")
        random_response = random.choice(responses)
        p2_streak = p2_streak + 1
    if p1_streak > p2_streak:
        await ctx.send(f"I bye <@!{player2.id}>")
        await player2.kick(reason=None)
        await player2.send(" Join back: https://discord.gg/*******************")
    if p2_streak > p1_streak:
        await ctx.send(f"Bye <@!{player1.id}>")
        await player1.kick(reason=None)
        await player1.send(" Join back: https://discord.gg/*******************")
    if p2_streak == p1_streak:
        await ctx.send(f"Draw, kicking someone random")
        if random_player == "a":
            await ctx.send(f"I bye <@!{player1.id}>")
            await player1.kick(reason=None)
            await player1.send(" Join back: https://discord.gg/*******************")
        if random_player == "b":
            await ctx.send(f"I bye <@!{player2.id}>")
            await player2.kick(reason=None)
            await player2.send(" Join back: https://discord.gg/*******************")

#Meme COMMAND
@bot.command(
    help="Meme.",
    brief="Mem.",
    pass_context=True,)


async def meme(ctx):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    top = subreddit.top(limit = 50)
    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    upvotes = submission.score

    meme = discord.Embed(title = name, url = url)

    meme.set_image(url=url)
    meme.set_footer(text=f"👍{upvotes}|💬LOADING REPLIES")
    await ctx.send(embed = meme)

@bot.command(
    help="AUTOMEMES.",
    brief="Dank.",
    pass_context=True,)


async def automeme(ctx, num_of_memes=20):
    subreddit = reddit.subreddit("memes")
    all_subs = []
    i = 0
    loading = discord.Embed(title="Loading Memes")
    loading.set_image(url="https://tenor.com/view/gif-21903508")
    embed = await ctx.send(embed=loading)
    top = subreddit.top(limit=500)
    embed.delete()
    while num_of_memes >= i:
        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        upvotes = submission.score

        meme = discord.Embed(title = name, url = url)

        meme.set_image(url=url)
        meme.set_footer(text=f"👍{upvotes}|💬LOADING REPLIES")
        await ctx.send(embed = meme)
        await asyncio.sleep(2.5)
        i = i+1


#UNIVERSAL COMMAND
@bot.command(
    help="Read the command",
    brief="Read the command",
    pass_context=True,)

async def howtodm(message):
    embedVar = discord.Embed(title="@beta testers can DM Anyone", description="Commands can also be used in private DMs", color=0x00ff00)
    embedVar.add_field(name="How to DM Anyone:", value="1. Turn On Developer Mode \n 2. Right-click on user you want to dm and *COPY ID* \n 3. say bot dm <@!*TARGETUSERID*> *your message*", inline=False)
    await message.channel.send(embed=embedVar)

@bot.command(pass_context=True)
async def giverole(ctx):
    guild = ctx.message.channel.guild
    role_id = *******************
    role = get(guild.roles, id=role_id)
    user= ctx.message.author
    await user.add_roles(role)

bot.run('*******************')

