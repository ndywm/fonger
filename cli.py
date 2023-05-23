from colorama import Fore,Style
from copy import deepcopy as dec
import fonger
print(Fore.LIGHTYELLOW_EX+"""
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣶⣿⣿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢠
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣛⣻⣿⣿⣟⣿⣿⣿⣷⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣽⣾⣻⣾⣿⣿⣿⣿⡿⣿⣿⠀⠀⠀
⠀⠀⠀⢰⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠻⡿⠿⠟⠛⣟⣿⣽⠀⠀⠀
⠀⠀⠀⠸⣿⣿⣿⣷⣿⣿⣿⣿⡿⠍⠈⠀⠁⣴⡆⠀⠀⠠⢭⣮⣿⡶⠀⠀
⠀⡴⠲⣦⢽⣿⣿⣿⣿⣿⣟⣩⣨⣀⡄⣐⣾⣿⣿⣇⠠⣷⣶⣿⣿⡠⠁⠀
⠀⠃⢀⡄⠀⢻⣿⣿⣿⣿⣽⢿⣿⣯⣾⣿⣿⣿⣿⣿⢿⣿⣿⡟⣿⠀⠀⠀
⠀⠀⠣⠧⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢸⣿⠿⠿⠿⣧⠙⣿⣿⡿⠀⠀⠀
⠀⠀⠀⠁⠼⣒⡿⣿⣿⣿⣿⣿⣿⣿⣠⣬⠀⠀⠀⠀⣾⣷⡈⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠉⢳⣿⣿⣿⣿⣿⣿⣿⢟⠗⠼⠖⠒⠔⠉⠉⠻⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣻⡿⣿⣿⣿⣿⡿⡀⣤⡄⠸⣰⣾⡒⣷⣴⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠂⢸⡗⡄⠘⠭⣭⣷⣿⣮⣠⣌⣫⣿⣷⣿⣿⠃⠀⠈⠀⠀
⠀⠀⠀⠀⠀⠈⠀⢸⣿⣾⣷⣦⡿⣿⣿⣿⡿⢻⠞⣹⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢘⠀⠘⢻⡿⢿⣋⣤⣤⠌⠉⠛⠛⠀⠈⠉⠁⠀⠀⠀⠀⠀⡀
    """)
print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"\ngwozdziu™ prezentuje\n")
print(Fore.LIGHTYELLOW_EX+"█████  ███  █   █  ███  █████ ████ ")
print(Fore.LIGHTYELLOW_EX+"█     █   █ ██  █ █     █     █   █")
print(Fore.LIGHTYELLOW_EX+"████  █   █ █ █ █ █  ██ ████  ████ ")
print(Fore.LIGHTYELLOW_EX+"█     █   █ █  ██ █   █ █     █ █  ")
print(Fore.LIGHTYELLOW_EX+"█      ███  █   █  ███  █████ █  ██   wersja beta")
print(Fore.LIGHTYELLOW_EX+"\nWitaj w praktycznym frontendzie do palcowania palców\n"+Style.NORMAL+Fore.RESET)


def throwwrongargs():
    print(Fore.LIGHTRED_EX+Style.BRIGHT+"Bad argumentós! Syntaxas sprawdzias!"+Fore.CYAN+Style.NORMAL)

AgainCommands=[]

def command_again(args):
    try:
        assert len(args)<2
        if args==[]:
            index=-1
        else:
            index=int(args[0])
        assert -1<=int(index)<len(AgainCommands)
        assert AgainCommands
    except:
        throwwrongargs()
        return
    args=AgainCommands[index]
    command=args[0]
    againargs=args[1]
    try:
        AgainCommands.append((command,dec(args)))
        exec(command+"(againargs)")
    except SyntaxError:
        print(Style.BRIGHT+Fore.LIGHTRED_EX+"Nie ma takiej komendy"+Fore.CYAN+Style.NORMAL)
    except NameError:
        print(Style.BRIGHT+Fore.LIGHTRED_EX+"Nie ma takiej komendy"+Fore.CYAN+Style.NORMAL)

def command_exit(args):
    print("dobranoc, do widzenia!"+Fore.RESET+Style.NORMAL)
    exit()

def command_add(args):
	try:
		assert len(args)==1
	except:
		throwwrongargs()
		return
	filename=fonger.addFingerprint(args[0])
	if filename is None:
		print(Style.BRIGHT+Fore.LIGHTRED_EX+"BŁĄÐ! Sprawdź, czy podłączono kamerę"+Fore.CYAN+Style.NORMAL)
	else:
		print(f"Zapisano nowy odcisk palca jako {filename}")

def command_ident(args):
    if len(args)==0:
        args=[None]
    for path in args:
        try:
            findOwnerResult=fonger.findOwner(path)
        except FileNotFoundError:
            print(Style.BRIGHT+Fore.LIGHTRED_EX+f"{path} nie istnieje!"+Fore.CYAN+Style.NORMAL)
            continue
        except OSError:
            print(Style.BRIGHT+Fore.LIGHTRED_EX+"BŁĄÐ! Sprawdź, czy podłączono kamerę"+Fore.CYAN+Style.NORMAL)
            return
        owner=findOwnerResult[0]
        bestScore=findOwnerResult[1]
        if owner is None:
            print("brak pasujących odcisków")
        else:
            print(f"Odcisk palca należy do {owner}, wynik: {bestScore}")



def command_set(args):
    try:
        assert len(args)==2
        variable=args[0]
        assert variable in {"X1","Y1","X2","Y2","ALPHA","BETA","cap","THRESHOLD","SENSITIVITY"}
        value=float(args[1])
    except:
        throwwrongargs()
        return
    try:
        if(variable=="cap"):
            exec(f"fonger.cap={cv2.VideoCapture(value)}")
        else:
            exec(f"fonger.{variable}={value}")
        print(f"sukces!")
    except:
        print(Style.BRIGHT+Fore.LIGHTRED_EX+"BŁĄÐ!"+Fore.CYAN+Style.NORMAL)
def strzala(a):
    a=str(a)
    strzala="}======------"
    return strzala[0:13-len(a)]+a+">>> "

def getCommand():
    print(Fore.LIGHTGREEN_EX+Style.BRIGHT+"{"+Fore.LIGHTWHITE_EX+"FONGER"+Fore.LIGHTGREEN_EX+strzala(len(AgainCommands))+Fore.LIGHTMAGENTA_EX+Style.NORMAL+"/",end="")
    try:
    	g=input().split()
    except KeyboardInterrupt:
    	print()
    	command_exit(None)
    print(Fore.CYAN,end="")
    return g


while True:
    command=getCommand()
    if(command==[]):
        continue
    args=command[1:]
    command="command_"+command[0]
    try:
        if(command!='command_again'):
            AgainCommands.append((command,dec(args)))
        exec(command+"(args)")
    except SyntaxError:
        print(Style.BRIGHT+Fore.LIGHTRED_EX+"Nie ma takiej komendy"+Fore.CYAN+Style.NORMAL)
    except NameError:
        print(Style.BRIGHT+Fore.LIGHTRED_EX+"Nie ma takiej komendy"+Fore.CYAN+Style.NORMAL)
