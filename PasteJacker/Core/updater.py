# -*- encoding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
from .color import *
from . import utils
from urllib.request import urlopen

def check():
	f = open( utils.add_corefilepath("Data","version.txt"), 'r')
	file_data = f.read().strip()
	try:
		version = urlopen('https://raw.githubusercontent.com/D4Vinci/PasteJacker/master/PasteJacker/Core/Data/version.txt').read().decode('utf-8').strip()
	except:
		error("Can't reach Internet !!!")
		sys.exit(0)

	if version != file_data:
		return file_data+R+" but new version is available!"
	else:
		return file_data
