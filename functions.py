
import os


class Content:
    def __init__(self) -> None:
        pass

    def getContent(ctx):
        obj = currentCommand.current_command
        if len(obj) > 1:
            obj.clear()
        currentCommand.current_command.append(ctx)


class currentCommand:
    current_command = []


class Command:
    def __init__(self) -> None:
        pass

#   using the os library it turns off your computer
    def turnOff():
        try:
            import os
            for i in range(6):
                string = f'PC TURNING OFF IN {6-i} SECONDS'
                print(string)
            os.system("shutdown -s")
        except Exception as e:
            return e
#   using the os library it puts your computer to sleep mode

    def sleep():
        try:
            import os
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
        except Exception as e:
            return e
#   using the os library it restarts your computer

    def restart():
        try:
            import os
            os.system("shutdown -r -t 0")
        except Exception as e:
            return e

#   using the subprocess library it executes a cmd command to check for active proceses, which it stores in proc.stdout
#   and we can loop throug them to list them all out *for line in proc.stdout*
    def taskManeger():
        try:
            import subprocess
            cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            open_apps = []
            for line in proc.stdout:
                if line.rstrip():
                    open_apps.append(line.decode().rstrip())
            return open_apps
        except Exception as e:
            return e

#   using a subprocess library to execute a powershell command to open an app
#   or a file (providet that the filepath is given)
    def run(app):
        try:
            import subprocess
            cmd = f'powershell "Start-Process {app}"'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            return proc
        except Exception as e:
            return e

#   using the os library it kills the provided aplication
    def forceStop(app):
        try:
            import os
            os.system(f'TASKKILL /F /IM {app} ')
        except Exception as e:
            return e

#   the screenShot function is made to take a full screen screenshot of your device, it creates its own folder in the
#   directory that you have put the main script file to which it saves the image (it also sends it to discord when it takes it)
    def screenShot(dir=os.getcwd(), folder='x43m1s_screenshots'):
        fullpath = f'{dir}\\{folder}'
        # print(fullpath)
        if not os.path.exists(fullpath):
            os.makedirs(fullpath)
        else:
            pass
        try:
            from mss import mss
            import datetime
            _time_ = datetime.datetime.now()
            name = f"{_time_.day}-{_time_.month}__{_time_.hour}-{_time_.minute}.png"
            with mss() as sct:
                sct.shot(output=f'{fullpath}\\{name}')
            return fullpath+'\\'+name
        except Exception as e:
            print(e)
            return e

#   opens a website :)
    def openWebsite(url=None):
        if url != None:
            url_ = f'https://www.{url}.com'
            try:
                import webbrowser
                webbrowser.open(url_)
            except Exception as e:
                return e
        else:
            return "None url given"

#   searches on youtube, and opens the first result
    def searchYT(query):
        try:
            from youtubesearchpython import VideosSearch as vhs
            search = vhs(query, limit=1)
            json_ = search.result()
            # get the link of the first of the search
            jsonDC = json_["result"][0]["link"]
            Command.openWebsite(None, jsonDC)

        except Exception as e:
            print(e)
            return e

#   using for loops it walks through the specified path and gets all the folders and files in that directory
    def seeFile(path: str, FF: str, skip: bool) -> list:
        folders = []
        files = []
        selected = []
        # if path is not spacefied it
        if path == None:
            path = os.getcwd()
        if FF == None:
            skip = False

        # checks for folders, files in the directory
        if os.path.exists(path):
            for item in os.listdir(path):
                if os.path.isdir(path+'\\'+item):
                    # if path is a folder it appends it to folder list
                    folders.append(item)
                else:
                    return_ = f"{item} | {os.path.join(path, item)}"
                    # if its a file it appends it to file list
                    files.append(return_)
            #  it goes through files to check for any files ending with requested ending and if they do, it adds them to selected list
            for item in files:
                if FF is not None:
                    if item.endswith(FF):
                        selected.append(item)
                    else:
                        pass
                else:
                    break
            if skip:
                return None, None, selected
            else:
                if selected == []:
                    return folders, files, None
                else:
                    return folders, files, selected
        else:
            return None, None, None

# special class exclusively for the timer function > schedule turning off/restarting/sleep your pc
class TIMER:
    def ChcFunc(f: str):
        if f.upper() == "OFF":
            return Command.turnOff()
        elif f.upper() == "RESTART":
            return Command.restart()
        elif f.upper() == "SLEEP":
            return Command.sleep()
        else:
            return None

    async def setTimer(file: str):
        import json
        import datetime
        import asyncio
        timer_settings = open(file, "r")
        data = json.load(timer_settings)
        time = data["time"]
        days = data["days"]
        exe = data["func"]
        while True:
            print("looping")
            current_time = datetime.datetime.now().strftime("%H:%M")
            print(f"{current_time} || {time}")
            if current_time == time:
                print("inside")
                if days != []:
                    for day in days:
                        current_day = datetime.datetime.now().strftime("%A")
                        if current_day == day:
                            TIMER.ChcFunc(exe)
                else:
                    TIMER.ChcFunc(exe)
            await asyncio.sleep(30)
