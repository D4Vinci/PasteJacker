# -*- coding: utf-8 -*-
# Written by: Karim shoair - D4Vinci
import os,sys
global G, Y, B, R, W , M , C , end ,Bold,underline
G,Y,B,R,W,M,C,end= '\033[92m','\033[93m','\033[94m','\033[91m','\x1b[37m','\x1b[35m','\x1b[36m','\033[0m'
Bold = "\033[1m"
underline = "\033[4m"

def numbered(n,text,spaces=2):
	if "(" in text and ")" in text:
		text = text.split("(")[0] +end+R+Bold +"(" +text.split("(")[1]
	return( " "*spaces+Bold+W+"["+G+str(n)+W+"] "+G+text+end )

def colored_input(title="menu",spaces=3):
	spaces = " "*spaces
	print(G+spaces+"│")
	line = G+spaces+"└──["+R+"PasteJacker"+G+"]──["+R+"~"+G+"]─["+B+title+G+"]: "+end
	return input(line)

def status(text):
	print( " "*2+C+"[+] "+Bold+G+text+end )

def error(text):
	print( " "*2+M+"[!] "+Bold+R+text+end )
