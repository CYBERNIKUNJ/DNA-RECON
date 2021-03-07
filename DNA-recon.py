#!/usr/bin/env python3  
import sys
import socket
import os
import time
from utility import menu
from modules import cms,Traceroute,reverseip,portscan,iplocation,httpheader,findsharedns,whois,dnslookup,robots,finder,cloudflare,wordpress



try:
    from colorama import Fore
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install colorama\n
    pip3 install colorama
        """)

#---------------------------

try:
    import requests
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install requests\n
    pip3 install requests
        """)

#---------------------------


try:
    import ipapi
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install ipapi\n
    pip3 install ipapi
        """)

#---------------------------


try:
    import builtwith
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install builtwith\n
    pip3 install builtwith
        """)

#---------------------------
while True:
    

    try:
        menu.Banner()
        menu.infolist1()
        number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DNA-recon"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ").lower()
    except:
        print("\n God Lock :) ")
        sys.exit()
    if number == '3':

        print
        sys.exit()
            
        #####################
        #####################

    elif number == "2":
        menu.infolist3()

        #####################

    elif number == "":
        print(Fore.RED+" [!]"+Fore.BLUE+" Please Enter Number :))))")
        input("")

#----------------------------------------------------------------------------------

#Information Gathering

    elif number == '1':
        try:
            menu.Banner()
            menu.infolist2()
            infor = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DNA-recon"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"Information Gathering"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ").lower()
    
           # if infor == "12":
            #    menu.Banner()
             #   cloudflare.__start__()

                #####################

            if infor == "9":
                menu.Banner()
                cms.__start__()

                #####################


            elif infor == "4":
                menu.Banner()
                Traceroute.__start__()

                #####################


            elif infor == "2":
                menu.Banner()
                reverseip.__start__()

                #####################

            elif infor == "3":
                menu.Banner()
                portscan.__start__()

                #####################
            
            elif infor == "5":
                menu.Banner()
                iplocation.__start__()

                #####################

            elif infor == "6":
                menu.Banner()
                httpheader.__start__()

                #####################

            elif infor == "7":
                menu.Banner()
                findsharedns.__start__()

                #####################

            elif infor == "1":
                menu.Banner()
                whois.__start__()    

                #####################

            elif infor == "8":
                menu.Banner()
                dnslookup.__start__()  
                #####################

            elif infor == "10":
                menu.Banner()
                robots.__start__()
                #####################

            elif infor == "11":
                menu.Banner()
                finder.__start__()

                #####################

            elif infor == "12":
                input(Fore.RED+" [!]"+Fore.GREEN+" Back To Menu (Press Enter...) ")

                #####################
            elif infor == "13":
                sys.exit()
                
                #####################
            elif infor == "":
                input(Fore.RED+" [!]"+Fore.GREEN+" Please Enter Number (Press Enter...) ")
        except KeyboardInterrupt:
            print("")
            sys.exit()

#------------------------------------------------------------------------------------------------
    elif number == "4":
        menu.infolist4()
        try:
            numcms = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DNA-recon"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"CMS Detection"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ").lower()

        except:
            print("")
            sys.exit()
        if numcms == "1":
            menu.infowp()
            try:
                wp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"DNA-recon"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"CMN"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"WordPress"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ").lower()
            except:
                print("")
                sys.exit()
            if wp == "1":
                menu.Banner()
                wordpress.wpplug()
            elif wp == "2":
                menu.Banner()
                wordpress.user()
            elif wp == "3":
                try:
                    input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
                except:
                    print("\n")
                    sys.exit()
        elif numcms == "2":
            menu.Banner()
            print(Fore.RED+" [!]"+Fore.BLUE+" Coming Soon ! ")
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()
        elif numcms == "3":
            menu.Banner()
            print(Fore.RED+" [!]"+Fore.BLUE+" Coming Soon ! ")
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()
        
        elif numcms == "4":
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()
        elif numcms == "" or False:
            try:
                input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
            except:
                print("")
                sys.exit()





