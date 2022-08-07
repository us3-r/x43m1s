
import os

class Content:
    def __init__(self) -> None:
        pass
    def getContent(ctx):
        obj=currentCommand.current_command
        if len(obj)>1:
            obj.clear()
        currentCommand.current_command.append(ctx)

class currentCommand:
    current_command=[]

class Command:
    def __init__(self) -> None:
        pass
    def turnOff():
        try:
            import os
            for i in range(6):
                string=f'PC TURNING OFF IN {6-i} SECONDS'
                print(string)
            os.system("shutdown -s")
        except Exception as e:
            return e
    def sleep():
        try:
            import os
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
        except Exception as e:
            return e
    def restart():
        try:
            import os
            os.system("shutdown -r -t 0")
        except Exception as e:
            return e
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
    def run(app):
        try:
            import subprocess
            cmd = f'powershell "Start-Process {app}"'
            proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            return proc
        except Exception as e:
            return e
    def forceStop(app):
        try:
            import os
            os.system(f'TASKKILL /F /IM {app} ')
        except Exception as e:
            return e
    def screenShot(dir=os.getcwd(), folder='x43m1s_screenshots'):
        fullpath=f'{dir}\\{folder}'
        # print(fullpath)
        if not os.path.exists(fullpath):
            os.makedirs(fullpath)
        else:pass
        try:
            from mss import mss
            import datetime
            _time_=datetime.datetime.now()
            name=f"{_time_.day}-{_time_.month}__{_time_.hour}-{_time_.minute}.png"
            with mss() as sct:
                sct.shot(output=f'{fullpath}\\{name}')
            return fullpath+'\\'+name
        except Exception as e:
            print(e)
            return e
    def openWebsite(url,yt=None):
        if yt==None:
            url_=f'https://www.{url}.com'

            try:
                import webbrowser
                webbrowser.open(url_)
            except Exception as e:
                return e
        elif url==None:
            try:
                import webbrowser
                webbrowser.open(yt)
            except Exception as e:
                return e


    def searchYT(query):
        try:
            from youtubesearchpython import VideosSearch as vhs
            search=vhs(query, limit=1)
            json_=search.result()
            jsonDC=json_["result"][0]["link"]
            Command.openWebsite(None,jsonDC)

        except Exception as e:
            print(e)
            return e


    def seeFile(path:str, FF:str, skip:bool ) -> list:
        folders=[]
        files=[]
        selected=[]
        if path==None:
            path=os.getcwd()
        if FF==None:
            skip=False
        print(f'>> {path}, {FF}, {skip}')
        if os.path.exists(path):
            for item in os.listdir(path):
                if os.path.isdir(path+'\\'+item):
                    folders.append(item)
                else:
                    return_ = f"{item} | {os.path.join(path, item)}"
                    files.append(return_)

            for item in files:
                if FF is not None:
                    if item.endswith(FF):
                            selected.append(item)
                    else:
                        pass
                else:break
            if skip:
                print("1")
                return None, None, selected
            else:
                if selected == []:
                    print("2")
                    return folders, files, None
                else:return folders, files, selected
        else:
            print("3")
            return None, None, None
