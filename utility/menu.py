import os
from colorama import Fore
import time
import sys
def Banner():

    os.system("clear")
    
    print(Fore.LIGHTRED_EX+"""\n    
          [ V 1.0 ] 
      
  ██████╗ ███╗   ██╗ █████╗ 
  ██╔══██╗████╗  ██║██╔══██╗
  ██║  ██║██╔██╗ ██║███████║
  ██║  ██║██║╚██╗██║██╔══██║
  ██████╔╝██║ ╚████║██║  ██║
  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝   
______ _____ _____ _____ _   _ 
| ___ \  ___/  __ \  _  | \ | |
| |_/ / |__ | /  \/ | | |  \| |
|    /|  __|| |   | | | | . ` |
| |\ \| |___| \__/\ \_/ / |\  |
\_| \_\____/ \____/\___/\_| \_/
	                                   
================================
**  Developer:~ NIKUNJ BHATT  **
================================      
""")  

def infolist1():
    time.sleep(0.1)
    print(Fore.RED+"["+Fore.WHITE+"卐"+Fore.RED+"]"+Fore.CYAN+" Choose one of the options below \n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [1] Information Gathering\n")
    time.sleep(0.1)
   # print(Fore.RED+" [2] CMS Detection\n") 
   # time.sleep(0.1)
    print(Fore.YELLOW+" [2] Creator \n")
    time.sleep(0.1)
    print(Fore.WHITE+" [3] Exit\n")






def infolist2():
    time.sleep(0.1)
    print(Fore.GREEN+"  [1]"+Fore.BLUE+" - Whois")    
    time.sleep(0.2)
    
    print(Fore.GREEN+"  [2]"+Fore.BLUE+" - Reverse IP")   
    time.sleep(0.1)

    print(Fore.GREEN+"  [3]"+Fore.BLUE+" - Port Scan")    
    time.sleep(0.1)
    
    print(Fore.GREEN+"  [4]"+Fore.BLUE+" - Trace Toute")   
    time.sleep(0.1)
    
    print(Fore.GREEN+"  [5]"+Fore.BLUE+" - IP location Finder")
    time.sleep(0.1)

    print(Fore.GREEN+"  [6]"+Fore.BLUE+" - Show HTTP Header")    
    time.sleep(0.1)

    print(Fore.GREEN+"  [7]"+Fore.BLUE+" - Find Shared DNS")    
    time.sleep(0.1)

    print(Fore.GREEN+"  [8]"+Fore.BLUE+" - DNS Lookup")   
    time.sleep(0.1)
    
    print(Fore.GREEN+"  [9]"+Fore.BLUE+" - Cms Detect")   
    time.sleep(0.1)

    print(Fore.GREEN+"  [10]"+Fore.BLUE+"- Robots Scanner")     
    time.sleep(0.1)

    print(Fore.GREEN+"  [11]"+Fore.BLUE+"- Admin Page Finder")    
    time.sleep(0.1)

   # print(Fore.GREEN+"  [12]"+Fore.BLUE+"- Bypass Cloud Flare")    
   # time.sleep(0.2)

    print(Fore.GREEN+"  [12]"+Fore.BLUE+"- Back To Menu")    
    time.sleep(0.1)

    print(Fore.GREEN+"  [13]"+Fore.WHITE+"- Exit \n")   

def infolist3():

      
      Banner()
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.BLUE+" Creator : NIKUNJ BHATT \n")
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.RED+" Website : https://bhattnikunj.com \n")
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.CYAN+" Telegram ID : @CYBERNIKUNJ \n")
      time.sleep(0.1)
      try:

            input(Fore.LIGHTRED_EX+" [*]  Back To Menu (Press Enter...) ")
      except:
            print("")
            print("\n")
            sys.exit()

def infolist4():

    Banner()
    
    print(Fore.GREEN+"  [1]"+Fore.BLUE+"- WordPress ")    
    time.sleep(0.1)

    print(Fore.GREEN+"  [2]"+Fore.BLUE+" - Drupal"+Fore.RED+" Coming Soon . . .")    
    
    time.sleep(0.1)

    print(Fore.GREEN+"  [3]"+Fore.BLUE+" - Joomla "+Fore.RED+" Coming Soon . . . ")    
    
    time.sleep(0.1)

    print(Fore.GREEN+"  [4]"+Fore.BLUE+" - Back To Menu")   
    
    print(Fore.CYAN+"  **********************\n")  
    time.sleep(0.1)


def infowp():
    Banner()
    
    print(Fore.GREEN+"  [1]"+Fore.BLUE+" - Get Plugins ")    
    time.sleep(0.1)

    print(Fore.GREEN+"  [2]"+Fore.BLUE+" - Get Username ")    
    time.sleep(0.1)

    print(Fore.GREEN+"  [3]"+Fore.BLUE+" - Back To Menu ")
    time.sleep(0.1)
