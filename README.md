# x43m1s
A program whit which you can, with a help of a discord bot use your computer from anywhere.


## COMMANDS

<br>‽ `Tasks` > shows open programs
<br>‽ `Turn off` > turn of your computer
<br>‽ `Sleep` > sleep your computer
<br>‽ `Restart` > restart your computer 

<br>‽ `Run "app-name.exe/file-path(C:/a/b/c/test.txt)` > open an app or a file
<br>‽ `Close "app-name/file-path(C:/a/b/c/test.txt)` > close an app or a file
<br>‽ `Shot` > get a live screenshot of your computer
<br>‽ `open :"website-name"` > opens a website
<br>‽ `search :"anythoing"` > searches for your input and opens the firs video on youtube
<br>‽ `cd | "directori" | "skip" | "file-format` > shows all files and folders in given directory, in you only wish to get specific files, specify that in "file-format" eg.(.txt) and set "T" to skip other files/folders (example: `cd | C:\a\b\c | F | `

## HOW TO RUN<br>

To run the main `(x43m1s.py)` file download the following libraries are required:
  <br>    -> 43req.txt using the `pip install -r 43req.txt` (or any other command)
<br>Or
<br>You can compile it into an ``.exe`` file eg.([auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/))
<br>By making a `.exe` file you can easily add the auto start option so the program starts as soon as you turn your computer on.

## HOW TO SET UP<br>
**DISCORD PART**<br>￣￣￣￣￣￣￣￣￣￣￣<br>

Firstly you will need a discord bot token
<br>> [Discord Developer portal](https://discord.com/developers/applications)
<br>
<br>Once you have your token you can create your private discord server, with at least one text channel in which you will write the commands
<br><br>Invite your bot to this server and the discord part is done :)

<br><br>CONFIG.json<br>￣￣￣￣￣￣￣￣￣￣￣<br>
```
{
    "DISCORD_TOKEN": "YOUR BOT ID", # your discord token [str]
    "ID": "YOUR ID", # your discord user ID [int]
    "CHANNEL": "CHANNEL ID", # ID of the channel you want your bot to send and read commands [int]
    "SERVER": "SERVER ID" # server ID [int]
}
```
<br><br>Lastly make shore that the `config.json` and `functions.py` are in the same directory as the `x43m1s.py`; If they are not make shore to change the lines:<br>**ln: 6** ` from functions import ` to ` from "path to functions.py" import *` <br>**ln: 10** `f=open('config.json','r')` to `f=open('path-to-config.json','r')`<br>



## TO DO
<br>× Add better error recognition if the app does not open
<br>× Add more commands 
