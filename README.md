# x43m1s
A program whit which you can, with a help of a discord bot use your computer from anywhere.


## COMMANDS
<br> COMPUTER MANAGE
<br>‽ `xtasks` > shows open programs
<br>‽ `xturnoff` > turn of your computer
<br>‽ `xsleep` > sleep your computer
<br>‽ `xrestart` > restart your computer
<br>‽ `xcd dir skip spec.files` > shows all files and folders in given directory, in you only wish to get specific files, specify that in "file-format" eg.(.txt) and set to "T" to skip other files/folders (example: `cd | C:\a\b\c | F | `
<br>
<br> TIMER (schedule when your pc turns off/restarts or goes to sleep
<br>‽ `xtimerstart action time days` > action(off,restart,sleep) | time(hh:mm) | days(any day of the week starting with capital letter)
<br>‽ `xtimerstop` > stops active timer
<br>‽ `xtimershow` > shows current timer settings (can be overwriten with `xtimerstart`)
<br>
<br> MISC
<br>‽ `xrun app-name.exe (or) C:/a/b/c/test.txt` > open an app or a file
<br>‽ `xclose app-name (or) C:/a/b/c/test.txt` > close an app or a file
<br>‽ `xshot` > get a live screenshot of your computer
<br>‽ `xopenweb "example"` > opens a website
<br>‽ `xopenyt "example"` > searches for your input and opens the firs video on youtube

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
<br>× Add option for multiple timers

## ISSUES
<br>× Issues with opening apps with only the filename given and are not in directory ("example.exe") 
