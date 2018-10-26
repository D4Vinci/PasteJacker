import os, socketserver, http.server, _thread as thread
from jinja2 import Environment, PackageLoader, FileSystemLoader
from . import utils
global httpd, directory_before_serve
httpd,directory_before_serve = [None]*2

def render(template_name,*args,**kwargs):
    env = Environment(loader=FileSystemLoader(searchpath=utils.get_templates_dir()))
    template = env.get_template(template_name)
    return template.render(*args,**kwargs)

def make_index(template_data):
    f = open("/root/.pastejacker/index.html","w")
    f.write(template_data)
    f.close()

def start_web_server(directory,port=80):
    global httpd, directory_before_serve
    class ReusableTCPServer(socketserver.TCPServer):
        allow_reuse_address = True
    # specify the httpd service on 0.0.0.0 (all interfaces) on port 80
    httpd = ReusableTCPServer( ("0.0.0.0", port), http.server.SimpleHTTPRequestHandler)
    directory_before_serve = os.getcwd()
    os.chdir(directory)
    thread.start_new_thread(httpd.serve_forever, ())

def stop_web_server():
    httpd.socket.close()
    os.chdir(directory_before_serve)
