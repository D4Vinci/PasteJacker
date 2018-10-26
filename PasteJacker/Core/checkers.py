import subprocess,os,socket

def msfvenom():
    cmd = subprocess.Popen("which msfvenom",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output,error=cmd.communicate()
    if error==output:
        return False
    return True

def our_folder():
    if not os.path.exists("/root/.pastejacker"):
        os.mkdir("/root/.pastejacker")

def port_in_use(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", port))
        s.close()
        return False # Port not in use
    except socket.error:
        s.close()
        return True # Port in use
