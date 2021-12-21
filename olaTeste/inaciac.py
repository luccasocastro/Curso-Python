import time
import pyshorteners
import os
from colorama import Fore,Back,Style
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)
clearConsole()

print(Fore.LIGHTYELLOW_EX+'''
  █████▒█    ██  ▄████▄   ██ ▄█▀    █    ██  ██▀███   ██▓    
▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒     ██  ▓██▒▓██ ▒ ██▒▓██▒    
▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░    ▓██  ▒██░▓██ ░▄█ ▒▒██░    
░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄    ▓▓█  ░██░▒██▀▀█▄  ▒██░    
░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄   ▒▒█████▓ ░██▓ ▒██▒░██████▒
 ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒   ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░
 ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░   ░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░
 ░ ░    ░░░ ░ ░ ░        ░ ░░ ░     ░░░ ░ ░   ░░   ░   ░ ░   
          ░     ░ ░      ░  ░         ░        ░         ░  ░
                ░                                            
''')
url = input(Fore.LIGHTGREEN_EX+"[@] insira o link >>> "+Fore.LIGHTRED_EX)

shrt = pyshorteners.Shortener()

nurl = shrt.tinyurl.short(url) 

print(Fore.LIGHTGREEN_EX+"[@] novo link >>> " +Fore.LIGHTBLUE_EX+nurl)

time.sleep(4)
print(Fore.LIGHTMAGENTA_EX+'''
coded by:                            
_         _         _   _   _
| |_ _ _ _| |___ ___| |_| |_| |_ _ ___ ___ ___ ___
| . | | | . | -_| .'|  _|   | |_'_|   |  _| -_|  _|
|___|_  |___|___|__,|_| |_|_|_|_,_|_|_|___|___|_|
    |___|
 ''' )