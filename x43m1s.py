from discord.ext import tasks
import discord
from discord import Embed, Member
from discord.ext import commands
from requests import request
import datetime
from functions import *
import json


f = open("config.json", 'r')
config = json.load(f)
CMD = False


TOKEN = config['DISCORD_TOKEN']
intents = discord.Intents.all()
intents.members = True
BOT = commands.Bot(command_prefix='$', intents=intents)

my_id = config["ID"]
listen_guild = config["SERVER"]
listen_channel = config["CHANNEL"]

_time_ = datetime.datetime.now()


@BOT.event
async def on_ready():
    await BOT.change_presence(activity=discord.Game(name="gaymin"))
    names__ = ""
    for guild in BOT.guilds:
        names__ = names__+"\t"+guild.name+" || "+str(guild.member_count)+"\n"
    print(f'[$]~>  BOT is in the following servers:\n\n{names__}')
    print(f'[$]~>  BOT is logged in as {BOT.user.name}')
    print(f'[$]~>  BOT is listening to {listen_guild}/{listen_channel}')


@BOT.command()
async def task(ctx):
    tasks = Command.taskManeger()
    Embed = discord.Embed(
        title=f"Task Maneger", description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
    channel = BOT.get_channel(listen_channel)
    for task in tasks:
        Embed.add_field(name=task, value='\0', inline=False)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def turnoff(ctx):
    Embed = discord.Embed(title=f"PC::state change::POWER-OFF ",
                          description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
    try:
        Command.turnOff()
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT SHUTING OFF YOUR PC :: {e}')

    Embed = discord.Embed(title=f"PC::state change::POWER-OFF ",
                          description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def sleep(ctx):
    Embed = discord.Embed(title=f"PC::state change::SLEEP  ",
                          description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
    await ctx.channel.send(embed=Embed)
    try:
        Command.sleep()
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT SLEEPING YOUR PC :: {e}')

    Embed = discord.Embed(title=f"PC::state change::SLEEP ",
                          description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def restart(ctx):
    await ctx.channel.send(f'{ctx.author.mention} is restarting your PC')
    try:
        Command.restart()
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT RESTARTING YOUR PC :: {e}')
    Embed = discord.Embed(title=f"PC::state change::RESTART ",
                          description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def timerstart(ctx, func: str = "off", time: str = None, day: str = None):
    import os
    available_functions = [
        "off",
        "restart",
        "sleep"
    ]
    if func in available_functions:
        try:
            os.mkdir("timer")
        except FileExistsError:
            pass
        file = f"timer\\const.json"
        if day != None:
            days = day.split(',')
        else:
            days = []
        import json
        timer_values = {
            "time": time,
            "days": days,
            "func": func
        }
        js_obj = json.dumps(timer_values, indent=4)
        with open(file, "w") as out_json:
            out_json.write(js_obj)
        Embed = discord.Embed(
            title=f"Starting timer :: [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]", description="______", color=0xf0e68c)
        Embed.add_field(name=":: Given values ::",
                        value=f"TIME ->{time}\nDAYS ->{days}\nACTION->{func}", inline=False)
        timerLoop.start()
        Embed.add_field(name="LOOP STARTED", value="success", inline=False)
        await ctx.channel.send(embed=Embed)
    else:
        await ctx.channel.send(f"**The function you requested is not supported:**\n*-> your function: {func}*\n-> available functions {available_functions}")


@BOT.command()
async def timerstop(ctx):
    timerLoop.cancel()
    Embed = discord.Embed(
        title=f"Stopping timer :: [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]", description="______", color=0xf0e68c)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def timershow(ctx):
    file = "timer\\const.json"
    timer_settings = open(file, "r")
    data = json.load(timer_settings)
    t = data["time"]
    d = data["days"]
    f = data["func"]
    Embed = discord.Embed(
        title=f"TIMER :: [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]", description="running timer", color=0xf0e68c)
    Embed.add_field(name=f"Time   :: {t}", value="..........", inline=False)
    Embed.add_field(name=f"Days   :: {d}", value="..........", inline=False)
    Embed.add_field(name=f"Action :: {f}", value="..........", inline=False)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def run(ctx, app: str):
    app = app
    Embed = discord.Embed(
        title=f"Opening App", description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
    Embed.add_field(name="Attempting to Open", value=app, inline=False)
    await ctx.channel.send(embed=Embed)
    try:
        Command.run(app)
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT OPENING {app} :: {e}')
    Embed = discord.Embed(
        title=f'{ctx.content} ', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    Embed.add_field(name=f'{ctx.author.mention} app :: {app}',
                    value='should be open now', inline=False)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def close(ctx, app: str):
    app = app
    if '.exe' in app:
        pass
    else:
        app = app+'.exe'
    Embed = discord.Embed(
        title=f"Close App", description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
    Embed.add_field(name="Attempting to close", value=app, inline=False)
    await ctx.channel.send(embed=Embed)

    try:
        Command.forceStop(app)
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT CLOSING {app} :: {str(e)}')

    Embed = discord.Embed(
        title=f'{ctx.content}', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    Embed.add_field(name=f'{ctx.author.mention} app :: {app}',
                    value='should be closed now', inline=False)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def shot(ctx):
    Embed = discord.Embed(
        title=f"Screenshot [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]", description=f"Request::{request}", color=0xf0e68c)
    await ctx.channel.send(embed=Embed)

    try:
        a = Command.screenShot()
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT SCREENSHOT :: {e}')
    Embed = discord.Embed(
        title=f"Screenshot", description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    file = discord.File(rf'{a}', filename='screenshot.png')
    Embed.set_image(url=f'attachment://{a}')
    await ctx.channel.send(embed=Embed, file=file)


@BOT.command()
async def openweb(ctx, url: str):
    url = url
    Embed = discord.Embed(
        title=f"Opening Website **{url}** ", description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
    await ctx.channel.send(embed=Embed)

    try:
        Command.openWebsite(url)
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT OPENING {url} :: {e}')

    Embed = discord.Embed(
        title=f'{ctx.content}', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    Embed.add_field(name=f'{ctx.author.mention} website :: {url}',
                    value='should be open now', inline=False)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def openyt(ctx, qury: str):
    Embed = discord.Embed(
        title=f"Searching Youtube [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]", description=f"Request::{request}", color=0xf0e68c)
    await ctx.channel.send(embed=Embed)
    qury = qury
    try:
        Command.searchYT(query=qury)
    except Exception as e:
        await ctx.channel.send(f'{ctx.author.mention} ERROR AT SEARCHING {qury} :: {e}')

    Embed = discord.Embed(
        title=f'{ctx.content}  [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', description="----", color=0x00ff00)
    Embed.add_field(name=f'{ctx.author.mention} query :: {qury}',
                    value='should be open in youtube now', inline=False)
    await ctx.channel.send(embed=Embed)


@BOT.command()
async def cd(ctx, path: str = os.getcwd(), skip: str = "F", select: str = None):
    image = ['.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp']
    text = ['txt', 'docx', 'doc', 'pdf', 'xlsx', 'xls', 'pptx', 'ppt']

    path = path
    if skip == "F":
        skip = False
    else:
        skip = True
    select = select

    # print(len(f1),len(f2),len(f3),len(f4),len(f5))
    Embed = discord.Embed(
        title=f'{ctx.content} ', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    Embed.add_field(name=f'{ctx.author.mention} path :: {path}',
                    value='Reading now', inline=False)
    await ctx.channel.send(embed=Embed)
    folders, files, selected = Command.seeFile(path, select, skip)
    # print(folders,files,selected)
    Embed = discord.Embed(
        title=f'{ctx.content} ', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
    Embed.add_field(name=f'PATH : : {path}',
                    value='Reading done', inline=False)
    Embed.add_field(name=f'￣￣￣￣￣￣￣￣￣￣￣|\nFOLDERS : : ',
                    value=f'⁓⁓⁓⁓~⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓~⁓⁓⁓', inline=False)
    if folders != None:
        inline_ = 0
        for i in folders:
            Embed.add_field(name=f'{i}', value=f'📁', inline=True)
    Embed.add_field(name=f'￣￣￣￣￣￣￣￣￣￣￣|\nFILES : : ',
                    value=f'⁓⁓⁓⁓~⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓~⁓⁓⁓', inline=False)
    if files != None:
        inline_ = 0
        for i in files:
            name = i.split('|')[0]
            path = i.split('|')[1]
            value = '🛠'
            for ending in image:
                if ending in name:
                    value = '🖼'
                    break
                else:
                    pass
            for ending in text:
                if ending in name:
                    value = f'📄'
                    break
                Embed.add_field(name=f'{name}', value=value, inline=True)
        Embed.add_field(name=f'￣￣￣￣￣￣￣￣￣￣￣|\nSELECTED : : ',
                        value=f'⁓⁓⁓⁓~⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓~⁓⁓⁓ ', inline=False)
        if selected != None:
            for i in selected:
                name = i.split('|')[0]
                path = i.split('|')[1]
                Embed.add_field(name=f'{name}', value=f'{path}', inline=True)
        await ctx.channel.send(embed=Embed)
    else:
        pass


@BOT.event
async def on_message(message):
    # await message.channel.purge(limit=1000000, check=lambda m: m.author == user)
    if message.author == BOT.user:
        return
    await BOT.process_commands(message)


@tasks.loop(minutes=1)
async def timerLoop():
    await TIMER.setTimer("timer\\const.json")
BOT.run(TOKEN)
