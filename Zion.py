import time as t
import os
import sys
from pystyle import Colors, Colorate
from colorama import Fore
import time

# Needed color stuff
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
red = Fore.RED
green = Fore.GREEN
reset = Fore.RESET
# End

# Update Config
VersionKey = ''

version = '3.1'
# End

# Update 

def checker():
  url = VersionKey
  r = requests.get(url, allow_redirects=True)
  with open('ServerKey.py', 'wb') as f:
    f.write(r.content)
    f.close()
  if Key == version:
    print("Up To Date !")
    t.sleep(3)
  else:
    print(f"Update needed ! \n Please hit option 3 in the main menu \n If you dont then the code will be outdated and buggy.")
    while True:
      option = input("")
      if option =='y':
        update()
      elif option =='Y':
        update()
      else:
        print("Please note there will be bugs .")
        break

# End

ascii = """
███████╗██╗ ██████╗ ███╗   ██╗
╚══███╔╝██║██╔═══██╗████╗  ██║
  ███╔╝ ██║██║   ██║██╔██╗ ██║
 ███╔╝  ██║██║   ██║██║╚██╗██║
███████╗██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝"""

bannerMALWARE = """
███████╗██╗ ██████╗ ███╗   ██╗
╚══███╔╝██║██╔═══██╗████╗  ██║
  ███╔╝ ██║██║   ██║██╔██╗ ██║
 ███╔╝  ██║██║   ██║██║╚██╗██║
███████╗██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝

+===================+
| 1.) Backdoor      |
| 2.) Ransomware    |
| 3.) Virus         |
| 4.) Rat (updated) |
| 99.) Go back      |
+===================+"""

banner = """
███████╗██╗ ██████╗ ███╗   ██╗
╚══███╔╝██║██╔═══██╗████╗  ██║
  ███╔╝ ██║██║   ██║██╔██╗ ██║
 ███╔╝  ██║██║   ██║██║╚██╗██║
███████╗██║╚██████╔╝██║ ╚████║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                              
+===================+
| 1.) Malware maker |
| 2.) View hosts    |
| 3.) Update        |
| 4.) Settings      |
| 5.) Exit          |
+===================+"""



def menu():
  print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))
  while True:
    option = input("> ")
    if option =='1':
      transition()
      malware()
    elif option =='2':
      sys.exit('coming soon !')
    elif option =='3':
      update()

def malware():
  print(Colorate.Horizontal(Colors.yellow_to_red, bannerMALWARE, 1))

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write(f"""\r{y}[{b}#{y}]{w} Loading... {i}""")
		sys.stdout.flush()
		time.sleep(0.2)

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def transition():
    clear()
    print(Colorate.Horizontal(Colors.yellow_to_red, ascii, 1))
    Spinner()
    clear()
	

if __name__ ==__name__:
  transition()
  menu()
