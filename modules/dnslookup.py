import sys
import requests
from colorama import Fore
import os
def __start__():

        try:
                print(Fore.RED+" [!] Enter The Domain\n")
                inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DNA-recon"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"NS-Lookup"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
                result = requests.get('http://api.hackertarget.com/dnslookup/?q=' + inp).text
                print(Fore.LIGHTBLUE_EX+result)
                try:
                        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
                except:
                        print("")
                        sys.exit()
        except:
                print("\n Exit :)")
                sys.exit()

