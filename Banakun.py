import os
import subprocess
from termcolor import colored
from pyfiglet import figlet_format
import time
	

def mainMenu():
    print((colored(figlet_format("                     Banakun"), color="red")))
    (print("\033[1;31m "))
    print("")
    time.sleep(1.2)
    print("========================== A tool by KuruKarova=================================")
    print("")
    time.sleep(1.5)
    print("==========================Made with python and lovee================================")
    print("")
    time.sleep(1.5)
    print("==========================WELCOME  TO  BANAKUN=====================================")
    
    
    
    print("\t\t\t1---> Host Discovery")
    print("\t\t\t2---> OS Discovery")
    print("\t\t\t3---> Port Discovery")
    print("\t\t\t4---> Port Discovery In Range")
    print("\t\t\t5---> Clear The Screen")
    print("\t\t\t6---> Quit The Program")
    
    choice = int(input("Select Your Option : "))
    if choice == 1:
        Host_DisCov()
        mainMenu()
    elif choice == 2:
        os_discovery()
        mainMenu()
    elif choice == 3:
        port_discovery()
        mainMenu()
    elif choice == 4:
        port_discoveryInRange()
        mainMenu()
    elif choice == 5:
         clear()
         mainMenu()
    elif choice == 6:
        clear()
        quit_Program()
    else:
        print("Invalid Choice :(")
        mainMenu()

	
def Host_DisCov():
    host=input("[*]Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-v', '-Pn', '-sn','-sL','-PE', '-PP','-oN','hostlist.txt', host])
    print('-' * 80)



def os_discovery():
    os = input("[*]Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-F','-A','-v', '-Pn','-sS','-O','-oN','os_Discove.txt', os])
    print('-' * 80)



def port_discovery():
    port = input("[*]Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap', '-n','-v', '-Pn', '-sV','-oN','Port_Discover.txt', port])
    print('-' * 80)



def port_discoveryInRange():
    port = input("[*]Enter Host Address To Scan : ")
    print('-' * 80)
    subprocess.check_call(
        ['nmap','-p','1-100','-oN','Port_DiscoverInRange.txt', port])
    print('-' * 80)

def clear():
    os.system('cls||clear')




def quit_Program():
    quit()




if __name__ == '__main__':
    mainMenu()
