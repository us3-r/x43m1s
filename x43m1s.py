import discord
from discord import Embed,Member
from discord.ext import commands
from requests import request
import datetime
from functions import *
import json


f=open('config.json','r')
config=json.load(f)
CMD=False


TOKEN=config['DISCORD_TOKEN']
intents = discord.Intents.all()
intents.members=True
BOT=commands.Bot(command_prefix='$', intents=intents)

my_id= config["ID"] 
listen_guild=config["SERVER"] 
listen_channel=config["CHANNEL"] 


_time_=datetime.datetime.now()

@BOT.event
async def on_ready():
    names__=""
    for guild in BOT.guilds:
        names__=names__+"\t"+guild.name+" || "+str(guild.member_count)+"\n"
    print(f'[$]~>  BOT is in the following servers:\n\n{names__}')
    print(f'[$]~>  BOT is logged in as {BOT.user.name}')
    print(f'[$]~>  BOT is listening to {listen_guild}/{listen_channel}')

@BOT.event
async def on_message(message):
    # await message.channel.purge(limit=1000000, check=lambda m: m.author == user)
    if message.author==BOT.user:
        return
    if message.author.id == my_id:
        if message.guild.id==listen_guild and message.channel.id==listen_channel:
            user = my_id
            content=message.content
            print(f'\n{content}')
            Content.getContent(content)

            # return current open tasks
            if content=='tasks' or content=='Tasks':
                tasks=Command.taskManeger()
                Embed=discord.Embed(title=f"Task Maneger", description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
                channel=BOT.get_channel(listen_channel)
                for task in tasks:
                    Embed.add_field(name=task, value='\0', inline=False)
                await message.channel.send(embed=Embed)
                await message.delete()

            # turn off PC
            elif content=='turn off' or content=='Turn off' or content=='off' or content=='Off':
                Embed=discord.Embed(title=f"PC::state change::POWER-OFF ",description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
                try:
                    Command.turnOff()
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT SHUTING OFF YOUR PC :: {e}')
                await message.delete()
                Embed=discord.Embed(title=f"PC::state change::POWER-OFF ",description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                await message.channel.send(embed=Embed)

            # sleep PC
            elif content=='sleep' or content=='Sleep':
                Embed=discord.Embed(title=f"PC::state change::SLEEP  ",description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
                await message.channel.send(embed=Embed)
                try:
                    Command.sleep()
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT SLEEPING YOUR PC :: {e}')
                await message.delete()
                Embed=discord.Embed(title=f"PC::state change::SLEEP ",description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                await message.channel.send(embed=Embed)

            # restart PC
            elif content=='restart' or content=='Restart':
                await message.channel.send(f'{message.author.mention} is restarting your PC')
                try:
                    Command.restart()
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT RESTARTING YOUR PC :: {e}')
                await message.delete()
                Embed=discord.Embed(title=f"PC::state change::RESTART ",description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                await message.channel.send(embed=Embed)

            # ############################################################################################# #
            #                                     EXECUTE STUFF ON PC                                       #
            # ############################################################################################# #

            # open app
            elif 'run' in message.content or 'Run' in message.content:
                app=message.content.split(':')[1]
                Embed=discord.Embed(title=f"Opening App", description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
                Embed.add_field(name="Attempting to Open", value=app, inline=False)
                await message.channel.send(embed=Embed)

                try:
                    Command.run(app)
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT OPENING {app} :: {e}')

                Embed=discord.Embed(title=f'{message.content} ', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                Embed.add_field(name=f'{message.author.mention} app :: {app}',value='should be open now',inline = False)
                await message.channel.send(embed=Embed)
                await message.delete()

            # close app
            elif 'close' in message.content or 'Close' in message.content:
                app=message.content.split(':')[1]
                if '.exe' in app:
                    pass
                else:
                    app=app+'.exe'
                Embed=discord.Embed(title=f"Close App",description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
                Embed.add_field(name="Attempting to close", value=app, inline=False)
                await message.channel.send(embed=Embed)

                try:
                    Command.forceStop(app)
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT CLOSING {app} :: {str(e)}')

                Embed=discord.Embed(title=f'{message.content}',description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]',color=0x00ff00)
                Embed.add_field(name=f'{message.author.mention} app :: {app}',value='should be closed now',inline = False)
                await message.channel.send(embed=Embed)
                await message.delete()

            # screenshot
            elif message.content.startswith('screenshot') or message.content.startswith('Screenshot') or message.content.startswith('shot') or message.content.startswith('Shot'):
                Embed=discord.Embed(title=f"Screenshot [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]", description=f"Request::{request}", color=0xf0e68c)
                await message.channel.send(embed=Embed)

                try:
                    a=Command.screenShot()
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT SCREENSHOT :: {e}')

                await message.delete()
                Embed=discord.Embed(title=f"Screenshot" ,description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                file=discord.File(rf'{a}', filename='screenshot.png')
                Embed.set_image(url=f'attachment://{a}')
                await message.channel.send(embed=Embed,file=file)

            # open website
            elif 'open website' in message.content or 'Open website' in message.content or 'open ' in message.content or 'Open ' in message.content:
                url=message.content.split(':')[1]
                Embed=discord.Embed(title=f"Opening Website **{url}** ",description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0xf0e68c)
                await message.channel.send(embed=Embed)

                try:
                    Command.openWebsite(url)
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT OPENING {url} :: {e}')

                Embed=discord.Embed(title=f'{message.content}', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                Embed.add_field(name=f'{message.author.mention} website :: {url}',value='should be open now',inline = False)
                await message.channel.send(embed=Embed)
                await message.delete()

            # search youtube
            elif 'search' in message.content or 'Search' in message.content:
                Embed=discord.Embed(title=f"Searching Youtube [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]", description=f"Request::{request}", color=0xf0e68c)
                await message.channel.send(embed=Embed)
                qury=message.content.split(':')[1]
                try:
                    Command.searchYT(query=qury)
                except Exception as e:
                    await message.channel.send(f'{message.author.mention} ERROR AT SEARCHING {qury} :: {e}')

                Embed=discord.Embed(title=f'{message.content}  [{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', description="----", color=0x00ff00)
                Embed.add_field(name=f'{message.author.mention} query :: {qury}',value='should be open in youtube now',inline = False)
                await message.channel.send(embed=Embed)
                await message.delete()

            elif 'cd' in message.content or 'Cd' in message.content:
                image=['.png','.jpg','.jpeg','.gif','.bmp','.tiff','.webp']
                text=['txt','docx','doc','pdf','xlsx','xls','pptx','ppt']
                try:
                    path=message.content.split(' ')[2]
                except IndexError:
                    path=None
                # test1=message.content.split(' ')[3]
                try:
                    skip=message.content.split(' ')[4]
                except IndexError:
                    skip=None
                # test3=message.content.split(' ')[5]
                try:
                    select=message.content.split(' ')[6]
                except IndexError:
                    select=None
                # print(f'{path} {skip} {select}')
                if skip=='t' or skip=='T':
                    skip=True
                else:
                    skip=False

                # print(len(f1),len(f2),len(f3),len(f4),len(f5))
                Embed=discord.Embed(title=f'{message.content} ', description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                Embed.add_field(name=f'{message.author.mention} path :: {path}',value='Reading now',inline = False)
                await message.channel.send(embed=Embed)
                folders,files,selected=Command.seeFile(path, select, skip)
                # print(folders,files,selected)
                Embed=discord.Embed(title=f'{message.content} ',description=f'[{_time_.day}.{_time_.month} || {_time_.hour}:{_time_.minute}]', color=0x00ff00)
                Embed.add_field(name=f'PATH : : {path}',value='Reading done',inline = False)
                Embed.add_field(name=f'￣￣￣￣￣￣￣￣￣￣￣|\nFOLDERS : : ', value=f'⁓⁓⁓⁓~⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓~⁓⁓⁓',inline = False)
                if folders!=None:
                    inline_=0
                    for i in folders:
                        Embed.add_field(name=f'{i}', value=f'📁',inline = True)
                Embed.add_field(name=f'￣￣￣￣￣￣￣￣￣￣￣|\nFILES : : ', value=f'⁓⁓⁓⁓~⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓~⁓⁓⁓',inline = False)
                if files!=None:
                    inline_=0
                    for i in files:
                        name=i.split('|')[0]
                        path=i.split('|')[1]
                        value='🛠'
                        for ending in image:
                            if ending in name:
                                value='🖼'
                                break
                            else:pass
                        for ending in text:
                            if ending in name:
                                value=f'📄'
                                break
                        Embed.add_field(name=f'{name}',value=value,inline = True)
                Embed.add_field(name=f'￣￣￣￣￣￣￣￣￣￣￣|\nSELECTED : : ', value=f'⁓⁓⁓⁓~⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓⁓~⁓⁓⁓ ',inline = False)
                if selected!=None:
                    for i in selected:
                        name=i.split('|')[0]
                        path=i.split('|')[1]
                        Embed.add_field(name=f'{name}',value=f'{path}',inline = True)
                await message.channel.send(embed=Embed)


            else:pass
    await BOT.process_commands(message)

BOT.run(TOKEN)



