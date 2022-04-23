import tempfile
import urllib.request
import subprocess
import threading
from pypresence import Presence
import uuid
from pathlib import Path
from urllib.request import urlopen, Request
import psutil
import wmi
from smsactivate.api import SMSActivateAPI
from twocaptcha import TwoCaptcha
import wget
from dhooks import Webhook
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import Select
import names
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
import os.path
from datetime import datetime
import random
import string
import os.path
from keyauth import api
import time
import colorama
import os, re, json, urllib.request, requests, datetime
from colorama import Fore, Style
import ctypes
from threading import Lock
from selenium.webdriver.common.proxy import Proxy, ProxyType
from multiprocessing import Lock, Value
import sys
import hashlib
from time import gmtime, strftime


colorama.init(autoreset=False)


def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
    	path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path,"rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return
start = strftime("%H:%M:%S", gmtime())
if os.path.isfile('log.txt'):
    os.remove("log.txt")
else:
    pass
with open("log.txt", "a") as f:
    print(f"(Start time: {start})", file=f)

print(Style.BRIGHT)

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
cls()

def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

ip = getip()


def slow_type(text, speed, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()


def Ip_Adress():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Logging In...]")

Logo = """╔╗╔╦  ╔╦╗  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
║║║║   ║║  ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
╝╚╝╩═╝═╩╝  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─"""
slow_type(f"{Logo}", 0.0001)
time.sleep(0.5)
slow_type(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Verify License Key... / Connecting to Discord RPC...", 0.04)
try:
    rpc = Presence("928283324525449276")
    rpc.connect()
    rpc.update(details="[Status: Logging In...]", large_image="logo", large_text="Made By 67")
    RPC_Connect = "True"
except Exception as E:
    time.sleep(1)
    RPC_Connect = "False"
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Couldn't connect to Discord RPC! [{E}]{Fore.RESET}")
    fdfadsfs = strftime("%H:%M:%S", gmtime())
    with open("log.txt", "a") as f:
        print(f"({fdfadsfs}) [ERROR] Couldn't connect to Discord RPC!", file=f)
time.sleep(1)
try:
    def get_user_inputs():

        settingspath = Path("settings.json")
        if settingspath.is_file():
             pass
        else:
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Not found 'settings.json', please add 'settings.json' to folder!")
            two = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"({two}) [ERROR] Not found 'settings.json']", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: 'settings.json' not found!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()
        with open('settings.json') as file:
            config_dictionary = json.load(file)

        LicenseKey = config_dictionary["LicenseKey"]
        Kuy = config_dictionary["LicenseKey"]
        def SendDiscordWebhook():
            try:
                from datetime import datetime

                serveruser = os.getenv("UserName")
                pc_name = os.getenv("COMPUTERNAME")
                mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
                computer = wmi.WMI()
                os_info = computer.Win32_OperatingSystem()[0]
                os_name = os_info.Name.encode('utf-8').split(b'|')[0]
                hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
                api = "https://discord.com/api/webhooks/950814920365182996/lQ6swfTWVteOI8N-yq2g4PCsLFszI3fhf8HPd1nfXKq325RfBoHsYVKlfxeKcnk3LL_1"

                webhooksend = Webhook(api)
                webhooksend.send(f"""
                **User Detect**```yaml
License Key: {Kuy}
PC Name: {pc_name}
PC Username: {serveruser}
HWID: {hwid}
IP: {ip}
MAC: {mac}
PLATFORM: {os_name}
CPU: {computer.Win32_Processor()[0].Name}
RAM: {str(round(psutil.virtual_memory().total / (1024.0 ** 3)))} GB
GPU: {computer.Win32_VideoController()[0].Name}
TIME: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}```""")
            except:
                pass

        SendDiscordWebhook()
        keyauthapp = api("", "", "", "", hash_to_check=None) # ("your application name", "your owner id", "your application secret","version")

        keyauthapp.license(LicenseKey)
        if RPC_Connect == "True":
            try:
                rpc.update(details="[Status: Successfully Logged In!]", large_image="logo", large_text="Made By 67")
            except:
                pass
        else:
            pass
        time.sleep(2.0)
        def ChromePath():
            chromepath = Path("chromedriver.exe")
            if chromepath.is_file():
                pass
            else:
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Not found 'chromedriver.exe'{Fore.RESET}")
                time.sleep(1.5)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Please Choose {Fore.LIGHTYELLOW_EX}YOUR{Fore.RESET} Current Google Chrome Version: """"
        1. Google Chrome Version: 96
        2. Google Chrome Version: 97
        3. Google Chrome Version: 98
        4. Google Chrome Version: 99
                    """"")
                AnsVersion = input("Select Option: ")
                if AnsVersion == "1":
                        wget.download('https://onedrive.live.com/download?cid=71AF184AC7C76CB1&resid=71AF184AC7C76CB1%21101346&authkey=AMvg3df5S8kCwgA')
                        time.sleep(0.5)
                        print()
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Successfully downloaded Google Chrome Version {Fore.LIGHTYELLOW_EX}96!{Fore.RESET}")
                        time.sleep(3)
                elif AnsVersion == "2":
                        wget.download('https://onedrive.live.com/download?cid=71AF184AC7C76CB1&resid=71AF184AC7C76CB1%21101349&authkey=AMisYktNJNd3Zdg')
                        time.sleep(0.5)
                        print()
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Successfully downloaded Google Chrome Version {Fore.LIGHTYELLOW_EX}97!{Fore.RESET}")
                        time.sleep(3)
                elif AnsVersion == "3":
                        wget.download('https://onedrive.live.com/download?cid=71AF184AC7C76CB1&resid=71AF184AC7C76CB1%21101351&authkey=AD1dxPmuOBHBeFg')
                        time.sleep(0.5)
                        print()
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Successfully downloaded Google Chrome Version {Fore.LIGHTYELLOW_EX}98!{Fore.RESET}")
                        time.sleep(3)
                elif AnsVersion == "4":
                        wget.download('https://onedrive.live.com/download?cid=71AF184AC7C76CB1&resid=71AF184AC7C76CB1%21101352&authkey=AGBN1p5H3ebmAFo')
                        time.sleep(0.5)
                        print()
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Successfully downloaded Google Chrome Version {Fore.LIGHTYELLOW_EX}99!{Fore.RESET}")
                        time.sleep(3)
                elif AnsVersion == "":
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Not Valid Option!{Fore.RESET}")
                        time.sleep(4)
                        FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"(End time: {FINIFJDSFSDF})", file=f)
                        sys.exit()
                elif AnsVersion != "":
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Not Valid Option!{Fore.RESET}")
                        time.sleep(4)
                        FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"(End time: {FINIFJDSFSDF})", file=f)
                        sys.exit()

        ChromePath()
        def cls():
                os.system('cls' if os.name == 'nt' else 'clear')
        cls()

        SecurityQuestion = config_dictionary["SecurityQuestion"]
        Auto_Captcha = config_dictionary["AutoCaptcha"]
        Accounts_To_Make = config_dictionary["Threads"]
        Headless = config_dictionary["Headless"]
        ProxCF = config_dictionary["UseProxy"]
        CaptchaBypass = config_dictionary["CaptchaBypass"]
        SmsService = config_dictionary["SmsService"]
        Threads = config_dictionary["Threads"]
        AutoSMS = config_dictionary["AutoSMS"]

        if AutoSMS != "On" and AutoSMS != "Off":
            dsfsdfslkfs = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} 'AutoSMS' in settings should be 'On' or 'Off'!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({dsfsdfslkfs}) [ERROR] 'AutoSMS' in settings should be 'On' or 'Off'!", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()
        if AutoSMS == "Off":
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Are you sure, you want Generate Account(s) {Fore.LIGHTYELLOW_EX}without Auto SMS verification{Fore.RESET}? (yes or no)")
            pAnsDelete = input("- Your Answer: ")
            if pAnsDelete == "yes":
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTYELLOW_EX} OK{Fore.RESET}")
                time.sleep(0.4)
            elif pAnsDelete == "no":
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTYELLOW_EX} OK{Fore.RESET}")
                time.sleep(2.6)
                sys.exit()
            elif pAnsDelete == "":
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} I said: {Fore.LIGHTRED_EX}yes or no{Fore.RESET}!")
                time.sleep(4)
                sys.exit()
            elif pAnsDelete != "":
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} I said: {Fore.LIGHTRED_EX}yes or no{Fore.RESET}!")
                time.sleep(4)
                sys.exit()
        if AutoSMS == "On":
            if SmsService != "smsactivate" and SmsService != "5sim":
                 dsfsdfslkfs = strftime("%H:%M:%S", gmtime())
                 print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} 'SmsService' in settings should be 'smsactivate' or '5sim'{Fore.RESET}")
                 with open("log.txt", "a") as f:
                    print(f"({dsfsdfslkfs}) [ERROR] 'SMSService' in settings should be 'smsactivate' or '5sim'!", file=f)
                 ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
                 FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                 with open("log.txt", "a") as f:
                     print(f"(End time: {FINIFJDSFSDF})", file=f)
                 time.sleep(4)
                 sys.exit()

            if SmsService == "5sim":
                try:
                    token = config_dictionary["5simApiKey"]
                    headers = {
                            'Authorization': 'Bearer ' + token,
                            'Accept': 'application/json',
                    }
                    response = requests.get('https://5sim.net/v1/user/profile', headers=headers)
                    Balance = json.loads(response.text)
                except Exception as a:
                    FOUR = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} 5sim error: {a}{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({FOUR}) [ERROR] 5sim Error: {a}", file=f)
                    FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"(End time: {FINIFJDSFSDF})", file=f)
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: 5sim Error!]")
                    time.sleep(4)
                    sys.exit()

            if SmsService == "smsactivate":
                try:
                    smsApi = config_dictionary["smsactivateApiKey"]
                    balance = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=getBalance"
                    requests.get(url=balance)
                except Exception as b:
                    time.sleep(0.3)
                    dsfsdfksf = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} SMSActivate error: {b}{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({dsfsdfksf}) [ERROR] SMSActivate error: {b}", file=f)
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: SMSActivate Error!]")
                    FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"(End time: {FINIFJDSFSDF})", file=f)
                    time.sleep(4)
                    sys.exit()

        if SecurityQuestion == "":
            SIX = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Please set 'Security Question' in settings!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({SIX}) [ERROR] No Security Question found in 'settings.json'", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()

        if Auto_Captcha != "On" and Auto_Captcha != "Off":
            SEVSKFD = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} 'Auto Captcha' in settings should be 'On' or 'Off'!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({SEVSKFD}) [ERROR] 'Auto Captcha' in settings should be 'On' or 'Off'!", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()


        if CaptchaBypass != "On" and CaptchaBypass != "Off":
            FDUSAFAFG = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} 'CaptchaBypass' in settings should be 'On' or 'Off'!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({FDUSAFAFG}) [ERROR] 'CaptchaBypass' in settings should be 'On' or 'Off'!", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()

        if CaptchaBypass == "On" and Auto_Captcha == "On":
            FDUSAFAFG = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} You can't have Captcha Bypass 'On' and Auto Captcha 'On'!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({FDUSAFAFG}) [ERROR] You can't have Captcha Bypass 'On' and Auto Captcha 'On'!", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(3)
            sys.exit()

        if Auto_Captcha == "Off":
            if CaptchaBypass == "On":
                tempfolder = tempfile.gettempdir()
                name = 'tokens.txt'
                completeName2 = os.path.join(tempfolder, name)
                if os.path.isfile(completeName2):
                    pass
                else:
                    KALJFA = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} No Captcha Tokens Found, please make them with 'Captcha_Token_Gen_v1.1.exe'! or turn On Auto Captcha!{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({KALJFA}) [ERROR] No Captcha Tokens found!", file=f)
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
                    FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"(End time: {FINIFJDSFSDF})", file=f)
                    time.sleep(4)
                    sys.exit()
                file1 = open(completeName2, 'r')
                file1.readlines()
                num_lines = sum(1 for line in open(completeName2))
                NUMB = config_dictionary["Threads"]
                AccToken = int(NUMB) - 1
                if num_lines <= 0:
                    KALJFA = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} No Captcha Tokens Found, please make them with 'Captcha_Token_Gen_v1.1.exe'! or turn On Auto Captcha!{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({KALJFA}) [ERROR] No Captcha Tokens found!", file=f)
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
                    FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"(End time: {FINIFJDSFSDF})", file=f)
                    time.sleep(4)
                    sys.exit()
                else:
                    pass

                if num_lines <= AccToken:
                    KALJFA = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Not enough Captcha Tokens found! [Captcha Tokens Found: {num_lines} - Threads: {Threads}] Please make them with 'Captcha_Token_Gen_v1.0.exe'! or turn On Auto Captcha!{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({KALJFA}) [ERROR] No Captcha Tokens found!", file=f)
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
                    FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"(End time: {FINIFJDSFSDF})", file=f)
                    time.sleep(4)
                    sys.exit()

        if Headless != "On" and Headless != "Off":
            FDUSAFAFG = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} 'Headless' in settings should be 'On' or 'Off'!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({FDUSAFAFG}) [ERROR] 'Headless' in settings should be 'On' or 'Off'!", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()

        if ProxCF == "":
            PROXFD = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} 'Proxy' in settings should be 'On' or 'Off'!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({PROXFD}) [ERROR] 'Proxy' in settings should be 'On' or 'Off'!", file=f)
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Something Went Wrong!]")
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()

        if Accounts_To_Make != "" and Accounts_To_Make != "0":
            Threads = "1"
            Accounts_To_Make = config_dictionary["Threads"]
        else:
            Accounts_To_Make = "1"
            FSFDF = strftime("%H:%M:%S", gmtime())
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Not valid number in Threads, Threads is set as default to '1'!{Fore.RESET}")
            with open("log.txt", "a") as f:
                print(f"({FSFDF}) [ERROR] Please enter valid number in Threads!", file=f)
            FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"(End time: {FINIFJDSFSDF})", file=f)
            time.sleep(4)
            sys.exit()

        Accounts_To_Make = int(Accounts_To_Make)
        return Accounts_To_Make
    def Account_Generator(The_Proxy=None, Locking_Thing_For_Proxy=None):
        global Threads, Country
        with open('settings.json') as file:
            config_dictionary = json.load(file)
        NumbCountry = config_dictionary["5simCountry"]
        AutoSMS = config_dictionary["AutoSMS"]
        NUMB = config_dictionary["Threads"]
        if NUMB == "1":
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Generating Account...]" + " {Accounts: 0/" + NUMB + " - Good 0 - Failed: 0}")
            if RPC_Connect == "True":
                try:
                    rpc.update(state="[Accounts: 0/" + NUMB + " - Failed: 0]", details="[Status: Generating Account...]", large_image="logo", large_text="Made By 67")
                except:
                    pass
        else:
            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Generating Accounts...]" + " {Accounts: 0/" + NUMB + " - Good 0 - Failed: 0}")
            if RPC_Connect == "True":
                try:
                    rpc.update(state="[Accounts: 0/" + NUMB + " - Failed: 0]", details="[Status: Generating Accounts...]", large_image="logo", large_text="Made By 67")
                except:
                    pass

        SMSService = config_dictionary["SmsService"]

        if AutoSMS == "On":
            if SMSService == "5sim":
                token = config_dictionary["5simApiKey"]
                country = config_dictionary["5simCountry"]
                operator = config_dictionary["5simOperator"]
                product = 'blizzard'
                headers = {
                    'Authorization': 'Bearer ' + token,
                    'Accept': 'application/json',
                }
                try:
                    response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)
                    data = json.loads(response.text)
                    id5sim = data['id']
                    PhoneNumber5sim = data['phone']
                    PhonePrice5sim = str(data['price']) + '₽'
                except Exception as c:
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} 5sim Error: {Fore.LIGHTRED_EX}{c}{Fore.RESET}")
                    FDSxgsd = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"({FDSxgsd}) [ERROR] 5sim error: {c}", file=f)
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    if NUMB == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str( AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    time.sleep(4)
                    sys.exit()
            if SMSService == "smsactivate":
                smsApi = config_dictionary["smsactivateApiKey"]
                country2 = config_dictionary["smsactivateCountry"]
                OperatorSMS = config_dictionary["smsactivateOperator"]
                service = 'bz'
                try:
                    buy = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=getNumber&service=" + service + "&operator=" + OperatorSMS + "&country=" + country2
                    responsebuy = requests.get(url=buy)
                    time.sleep(0.4)
                    data = responsebuy.text
                    PhoneSMSActivate = data.split(':')
                    PhoneSMSActivate = PhoneSMSActivate[2]
                    idActivate = data.split(':')
                    idActivate = idActivate[1]
                except Exception as d:
                    dfidfsfqw = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} SMSActivate Error: {Fore.LIGHTRED_EX}{d}{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({dfidfsfqw}) [ERROR] SMSActivate Error: {d}", file=f)
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    if NUMB == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str( AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    time.sleep(4)
                    sys.exit()

                sa = SMSActivateAPI(smsApi)
                sa.debug_mode = False
                prices = sa.getPrices(service=service, country=country2)
                try:
                    countryTest = prices[country2]
                    bliz = countryTest['bz']
                    test = bliz['cost']
                    PriceSMS = str(test) + '₽'
                except:
                    pass
        def FinishOrderSmsActivate():
            try:
                cancel = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=setStatus&status=" + "6&id=" + idActivate
                requests.get(url=cancel)
                time.sleep(0.3)
            except:
                pass
            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Finishing{Fore.RESET} SMSActivate Order...")
            time.sleep(0.2)
        def FinishOrder5sim():
            try:
                requests.get('https://5sim.net/v1/user/finish/' + str(id5sim), headers=headers)
            except:
                pass
            print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Finishing{Fore.RESET} 5sim Order...")
            time.sleep(0.2)
        def CancelsOrder5sim():
            headers = {
                'Authorization': 'Bearer ' + token,
                'Accept': 'application/json',
            }
            try:
                requests.get('https://5sim.net/v1/user/cancel/' + str(id5sim), headers=headers)
            except:
                pass
            print()
            print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Cancel{Fore.RESET} 5sim Order......")
            time.sleep(0.2)
        def CancelsOrderActivate():
            try:
                cancel = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=setStatus&status=8&id=" + idActivate
                requests.get(url=cancel)
                time.sleep(0.3)
            except:
                pass
            print()
            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Cancel{Fore.RESET} SMSActivate Order.......")
            time.sleep(0.2)
        def SendOrderSMSActivate():
            try:
                cancel = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=setStatus&status=1&id=" + idActivate
                requests.get(url=cancel)
                time.sleep(0.3)
            except:
                pass
            print(Fore.LIGHTMAGENTA_EX + "[SMS]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" +Fore.LIGHTYELLOW_EX + " Sending" + Fore.RESET + " SMSActivate Order...")

        # Auto captcha on or off
        Auto_Captcha = config_dictionary["AutoCaptcha"]
        start_time = time.time()
        # Chrome settings

        Headless = config_dictionary["Headless"]
        if The_Proxy != None:
            The_Proxy_Separated_List = The_Proxy.split(":")
            if len(The_Proxy_Separated_List) != 2:
                FailedAccValue.value += 1
                AccGenedValue.value += 1
                ADFX = config_dictionary["Threads"]
                if NUMB == "1":
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(
                                state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                    FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                large_image="logo", large_text="Made By 67")
                        except:
                            pass
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str( AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(
                                state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                    FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                large_image="logo", large_text="Made By 67")
                        except:
                            pass
                # raise ValueError()

            with Locking_Thing_For_Proxy:
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = The_Proxy
                prox.ssl_proxy = The_Proxy

                proxy = prox.http_proxy
                proxies = proxy.split(':')
                proxy_split = proxies[0]

                def get(ip):
                    endpoint = f'https://ipinfo.io/{ip}/json'
                    response = requests.get(endpoint, verify=True)

                    data = response.json()

                    return data['country']

                proxy_ip_country = get(proxy_split)

                capabilities = webdriver.DesiredCapabilities.CHROME
                capabilities = DesiredCapabilities.CHROME.copy()
                capabilities['goog:loggingPrefs'] = {'performance': 'INFO'}
                prox.add_to_capabilities(capabilities)

                Auto_Captcha = config_dictionary["AutoCaptcha"]

                try:
                    prefs = {
                        "intl.accept_languages": "en,en_US",
                        "credentials_enable_service": False,
                        "enable_do_not_track": True,
                        "profile.password_manager_enabled": False,
                        "webrtc.ip_handling_policy": "disable_non_proxied_udp",
                        "webrtc.multiple_routes_enabled": False,
                        "webrtc.nonproxied_udp_enabled": False,
                        "profile.default_content_setting_values.geolocation": 2
                    }
                    from fake_useragent import UserAgent
                    ua = UserAgent()
                    user_agent = ua.random
                    #  print(user_agent)
                    chrome_options = ChromeOptions()
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument('--ignore-certificate-errors')
                    chrome_options.set_capability('acceptInsecureCerts', True)
                    chrome_options.add_argument(f'user-agent={user_agent}')
                    chrome_options.add_argument("--no-sandbox")
                    chrome_options.add_argument("--disable-dev-shm-usage")
                    chrome_options.add_argument('--disable-extensions')
                    chrome_options.add_experimental_option('useAutomationExtension', False)
                    chrome_options.add_argument("--disable-plugins-discovery");
                    chrome_options.add_argument("disable-popup-blocking")
                    chrome_options.add_argument('--disable-gpu')

                    CaptchaBypass2 = config_dictionary["CaptchaBypass"]
                    if Headless == "On":
                        if Auto_Captcha == "Off" and CaptchaBypass2 == "Off":
                                pass
                        else:
                            chrome_options.add_argument('--headless')

                    chrome_options.add_argument("--incognito")
                    chrome_options.add_argument("--disable-dev-shm-usage")
                    chrome_options.add_argument("--window-size=350,600")
                    chrome_options.add_argument('--disable-extensions')
                    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
                    web = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options, desired_capabilities=capabilities)
                    web.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                    web.execute_script('return navigator.webdriver')
                    print(f"{Fore.LIGHTBLUE_EX}[PROXY]{Fore.RESET} [{threading.currentThread().getName()}] Using Proxy: {Fore.LIGHTYELLOW_EX}{prox.http_proxy}{Fore.RESET} [{proxy_ip_country}]")

                except Exception as e:
                    NEGE = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTBLUE_EX}[INFO]{Fore.RESET} Google Error:{Fore.LIGHTRED_EX} {e}{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({NEGE}) [ERROR] Google Error: {e}",file=f)
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Something Went Wrong!] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(
                                state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                    FailedAccValue.value) + "]", details="[Status: Something Went Wrong!]",
                                large_image="logo", large_text="Made By 67")
                        except:
                            pass
                    if AutoSMS == "On":
                        if SMSService == "5sim":
                            CancelsOrder5sim()
                        if SMSService == "smsactivate":
                            CancelsOrderActivate()
                    print(f"{Fore.LIGHTBLUE_EX}[INFO]{Fore.RESET} Delete 'chromedriver.exe', and run the Generator again and choose your Google Chrome Version when the Generator \nask to select Google Chrome Version!")
                    time.sleep(4)
                    sys.exit()

        else:
                # print(Fore.LIGHTBLUE_EX + "[IP]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + " Using IP: " + Fore.LIGHTYELLOW_EX + ip + Fore.RESET + " {" + ip_country + "}")
            try:
                prefs = {
                    "intl.accept_languages": "en,en_US",
                    "credentials_enable_service": False,
                    "enable_do_not_track": True,
                    "profile.password_manager_enabled": False,
                    "webrtc.ip_handling_policy": "disable_non_proxied_udp",
                    "webrtc.multiple_routes_enabled": False,
                    "webrtc.nonproxied_udp_enabled": False,
                    "profile.default_content_setting_values.geolocation": 2
                }

                from fake_useragent import UserAgent
                ua = UserAgent()
                user_agent = ua.random
                capabilities = DesiredCapabilities.CHROME.copy()
                capabilities['goog:loggingPrefs'] = {'performance': 'INFO'}
                #  print(user_agent)
                chrome_options = ChromeOptions()
                chrome_options.add_experimental_option("prefs", prefs)
                chrome_options.add_argument('--ignore-certificate-errors')
                chrome_options.set_capability('acceptInsecureCerts', True)
                chrome_options.add_argument(f'user-agent={user_agent}')
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument('--disable-extensions')
                chrome_options.add_argument("--disable-plugins-discovery")
                chrome_options.add_experimental_option('useAutomationExtension', False)
                chrome_options.add_argument("disable-popup-blocking")

                CaptchaBypass2 = config_dictionary["CaptchaBypass"]
                if Headless == "On":
                    if Auto_Captcha == "Off" and CaptchaBypass2 == "Off":
                        pass
                    else:
                        chrome_options.add_argument('--headless')

                chrome_options.add_argument("--incognito")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument('--disable-blink-features=AutomationControlled')
                chrome_options.add_argument("--window-size=350,600")
                chrome_options.add_argument("disable-notifications")
                chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
                web = webdriver.Chrome(executable_path='chromedriver.exe', options=chrome_options, desired_capabilities=capabilities)
                web.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                web.execute_script('return navigator.webdriver')
            except Exception as f:
                TWEDFG = strftime("%H:%M:%S", gmtime())
                print(f"{Fore.LIGHTBLUE_EX}[INFO]{Fore.RESET} Google Error: {Fore.LIGHTRED_EX}{f}{Fore.RESET}")
                with open("log.txt", "a") as f:
                    print(f"({TWEDFG}) [ERROR] Google Error: {f}", file=f)
                FailedAccValue.value += 1
                AccGenedValue.value += 1
                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Something Went Wrong!] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                if RPC_Connect == "True":
                    try:
                        rpc.update(
                            state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                FailedAccValue.value) + "]", details="[Status: Something Went Wrong!]",
                            large_image="logo", large_text="Made By 67")
                    except:
                        pass
                if AutoSMS == "On":
                    if SMSService == "5sim":
                        CancelsOrder5sim()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate()
                print(f"{Fore.LIGHTBLUE_EX}[INFO]{Fore.RESET} Delete 'chromedriver.exe', and run the Generator again and choose your Google Chrome Version when the Generator \nask to select Google Chrome Version!")
                time.sleep(4)
                sys.exit()

        Proxies = config_dictionary["UseProxy"]
        if Proxies == "On":
            pass
        else:
            def getip():
                ip = "None"
                try:
                    ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
                except:
                    pass
                return ip
            ip = getip()
            def get(ip):
                endpoint = f'https://ipinfo.io/{ip}/json'
                response = requests.get(endpoint, verify=True)
                data = response.json()
                return data['country']

            ip_country = get(ip)
            print(Fore.LIGHTBLUE_EX + "[IP]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + " Using IP: " + Fore.LIGHTYELLOW_EX + ip + Fore.RESET + " {" + ip_country + "}")
        web.get('https://account.battle.net/creation/flow/creation-full')

        time.sleep(0.2)

        # web.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

        # Generate random Email / Password
        def LastEmail(length=6, uppercase=False, lowercase=False, numbers=True):
                character_set = ''
                if numbers:
                    character_set += string.digits
                return ''.join(random.choice(character_set) for i in range(length))

        FirstEmail = names.get_first_name()
        MiddelEmail = names.get_last_name()

        def random_password_string(length=15, uppercase=True, lowercase=True, numbers=True):
                character_set = ''
                if uppercase:
                    character_set += string.ascii_uppercase
                if lowercase:
                    character_set += string.ascii_lowercase
                if numbers:
                    character_set += string.digits
                return ''.join(random.choice(character_set) for i in range(length))

        # Settings
        # password = random_password_string(length=15, uppercase=True, lowercase=True, numbers=True)
        Email = FirstEmail + MiddelEmail + LastEmail()
        FirstName = config_dictionary["FirstName"]
        LastName = config_dictionary["LastName"]
        Domain = "@" + config_dictionary["EmailDomain"]
        SecurityQuestion = config_dictionary["SecurityQuestion"]
        BattlePass = config_dictionary["BattleNetPassword"]
        BattleN = config_dictionary["BattleNetName"]
            # DBD
        day = random.randint(10, 12)
        month = random.randint(10, 12)
        year = random.randint(1970, 1998)

         ###############################################################################################################################################################################
        def PhoneNumberAlreadyUsed():
            country2 = config_dictionary["5simCountry"]
            try:
                time.sleep(0.2)
                nmberused = web.find_element_by_xpath('//*[@id="capture-phone-number"]')
                nmberused.click()
                time.sleep(0.1)
                nmberused.clear()
                time.sleep(0.1)
                if SMSService == "5sim":
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] Requesting Phone Number Again...")
                if SMSService == "smsactivate":
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] Requesting Phone Number Again...")

                BattleN = config_dictionary["BattleNetName"]
                if BattleN == "":
                    BattleN = names.get_last_name()
                else:
                     BattleN = config_dictionary["BattleNetName"]
                     if BattleN == "Random":
                        BattleN = names.get_last_name()
                     else:
                        BattleN = config_dictionary["BattleNetName"]
                if SMSService == "5sim":
                    token = config_dictionary["5simApiKey"]
                    country = config_dictionary["5simCountry"]
                    operator = config_dictionary["5simOperator"]
                    product = 'blizzard'

                    headers = {
                        'Authorization': 'Bearer ' + token,
                        'Accept': 'application/json',
                    }
                    NUMB = config_dictionary["Threads"]
                    try:
                        response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product,headers=headers)
                        data5sim2 = json.loads(response.text)
                        id5sim2 = data5sim2['id']
                        PhoneNumber5sim2 = data5sim2['phone']
                        PhonePrice5sim2 = str(data5sim2['price']) + '₽'
                    except Exception as g:
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} 5sim Error: {Fore.LIGHTRED_EX}{g}{Fore.RESET}")
                        FDSxgsd = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"({FDSxgsd}) [ERROR] 5sim error: {g}", file=f)
                        FailedAccValue.value += 1
                        AccGenedValue.value += 1
                        if Threads == "1":
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(
                                        state="[Accounts: " + str(
                                            AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                            FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                        large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        else:
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(
                                        state="[Accounts: " + str(
                                            AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                            FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                        large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        web.close()
                        time.sleep(4)
                        sys.exit()
                if SMSService == "smsactivate":
                    smsApi = config_dictionary["smsactivateApiKey"]
                    country2 = config_dictionary["smsactivateCountry"]
                    OperatorSMS2 = config_dictionary["smsactivateOperator"]
                    service = 'bz'
                    try:
                        buy = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=getNumber&service=" + service + "&operator=" + OperatorSMS2 + "&country=" + country2
                        responsebuy2 = requests.get(url=buy)
                        time.sleep(0.2)
                        data2 = responsebuy2.text
                        PhoneSMSActivate2 = data2.split(':')
                        PhoneSMSActivate2 = PhoneSMSActivate2[2]
                        idActivate2 = data2.split(':')
                        idActivate2 = idActivate2[1]
                    except Exception as h:
                        dfidfsfqw = strftime("%H:%M:%S", gmtime())
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} SMSActivate Error: {Fore.LIGHTRED_EX}{h}{Fore.RESET}")
                        with open("log.txt", "a") as f:
                            print(f"({dfidfsfqw}) [ERROR] SMSActivate Error: {h}", file=f)
                        FailedAccValue.value += 1
                        AccGenedValue.value += 1
                        if Threads == "1":
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(
                                        state="[Accounts: " + str(
                                            AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                            FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                        large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        else:
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(
                                        state="[Accounts: " + str(
                                            AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                            FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                        large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        web.close()
                        time.sleep(4)
                        sys.exit()

                def CancelFiveSImOrder2():
                    headers = {
                        'Authorization': 'Bearer ' + token,
                        'Accept': 'application/json',
                    }
                    try:
                        requests.get('https://5sim.net/v1/user/cancel/' + str(id5sim2), headers=headers)
                    except:
                        pass
                    print()
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Cancel{Fore.RESET} 5sim Order........")
                    time.sleep(0.2)

                def CancelsOrderActivate2():
                    try:
                        cancel = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=setStatus&status=8&id=" + idActivate2
                        requests.get(url=cancel)
                        time.sleep(0.3)
                    except:
                        pass
                    print()
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Cancel{Fore.RESET} SMSActivate Order........")
                    time.sleep(0.2)

                def FinishOrder5sim2():
                    try:
                        requests.get('https://5sim.net/v1/user/finish/' + str(id5sim2), headers=headers)
                    except:
                        pass
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Finishing{Fore.RESET} 5sim Order...")
                    time.sleep(0.2)

                def FinishOrderSmsActivate2():
                    try:
                        cancel = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=setStatus&status=6&id=" + idActivate2
                        requests.get(url=cancel)
                        time.sleep(0.3)
                    except:
                        pass
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Finishing{Fore.RESET} SMSActivate Order...")
                    time.sleep(0.2)

                def SendOrderSMSActivate2():
                    try:
                        cancel = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=setStatus&status=1&id=" + idActivate2
                        requests.get(url=cancel)
                    except:
                        pass
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Sending{Fore.RESET} SMSActivate Order...")

                time.sleep(0.2)
                numxf = web.find_element_by_xpath('//*[@id="capture-phone-number"]')
                numxf.click()
                time.sleep(0.2)
                if SMSService == "5sim":
                    numxf.send_keys(PhoneNumber5sim2)
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] Phone Number is set to: {Fore.LIGHTYELLOW_EX}{PhoneNumber5sim2}{Fore.RESET} [Price: {PhonePrice5sim2}]")
                if SMSService == "smsactivate":
                    numxf.send_keys(PhoneSMSActivate2)
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] Phone Number is set to: {Fore.LIGHTYELLOW_EX}{PhoneSMSActivate2}{Fore.RESET} [Price: {PriceSMS}]")
                time.sleep(0.2)
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.8)
                if SMSService == "smsactivate":
                    SendOrderSMSActivate2()
                if "Phone number is already in use" in web.page_source:
                    PAIDPAIDFD = strftime("%H:%M:%S", gmtime())
                    if SMSService == "5sim":
                        print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Phone Number Already is been used!{Fore.RESET}")
                        with open("log.txt", "a") as f:
                            print(f"({PAIDPAIDFD}) [ERROR] [{threading.currentThread().getName()}] 5sim Phone Number already is been used!", file=f)
                    if SMSService == "smsactivate":
                        print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Phone Number Already is been used!{Fore.RESET}")
                        with open("log.txt", "a") as f:
                            print(f"({PAIDPAIDFD}) [ERROR] [{threading.currentThread().getName()}] SMSActivate Phone Number already is been used!", file=f)
                    time.sleep(0.3)
                    if SMSService == "5sim":
                        CancelFiveSImOrder2()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate2()
                    PhoneNumberAlreadyUsed()
                else:
                    pass
                time.sleep(0.3)
                if "Please enter a post-paid phone number." in web.page_source:
                    OAPIFA = strftime("%H:%M:%S", gmtime())
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    if Threads == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    if SMSService == "smsactivate":
                        with open("log.txt", "a") as f:
                            print(f"({OAPIFA}) [ERROR] [{threading.currentThread().getName()}] Phone number is post-paid!",file=f)
                        time.sleep(0.2)
                        print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET}{Fore.LIGHTRED_EX} Phone number is post-paid!{Fore.RESET}", end="\r")
                    if SMSService == "5sim":
                        with open("log.txt", "a") as f:
                            print(f"({OAPIFA}) [ERROR] [{threading.currentThread().getName()}] Phone number is post-paid!",file=f)
                        time.sleep(0.2)
                        print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET}{Fore.LIGHTRED_EX} Phone number is post-paid!{Fore.RESET}", end="\r")
                    web.close()

                    if SMSService == "5sim":
                        CancelFiveSImOrder2()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate2()
                    time.sleep(3)
                    sys.exit()
                else:
                    pass
                time.sleep(0.9)

                if "Whoops! Something went wrong." in web.page_source:
                    time.sleep(0.2)
                    WHOOPSFD = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                            print(f"({WHOOPSFD}) [ERROR] [{threading.currentThread().getName()}] 'Whoops! Something went wrong.', try switch VPN Connection or switch proxies!",file=f)
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} try switch VPN Connection or switch proxies!{Fore.RESET}", end="\r")
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    if Threads == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    web.close()
                    time.sleep(0.2)
                    if SMSService == "5sim":
                        CancelFiveSImOrder2()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate2()
                    time.sleep(3)
                    sys.exit()
                else:
                    pass
                time.sleep(0.5)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resend-sms-verification"]')))
                time.sleep(0.3)
                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                print(end=LINECLEAR)
                if SMSService == "5sim":
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [0/50] Resend SMS Code...",end="\r")
                if SMSService == "smsactivate":
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [0/50] Resend SMS Code...", end="\r")
                time.sleep(1)
                if SMSService == "5sim":
                    count5sim2 = 1
                    if phone := 1:
                        codeInp5sim2 = ""
                    while (count5sim2 < 51, (requests.get('https://5sim.net/v1/user/check/' + str(id5sim2), headers=headers))):
                        response = requests.get('https://5sim.net/v1/user/check/' + str(id5sim2), headers=headers)
                        data = json.loads(response.text)
                        if (data['status'] == "RECEIVED"):
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim2)}/50] Waiting for SMS Code...", end="\r")
                            count5sim2 = count5sim2 + 1
                            time.sleep(1)
                            if (data['sms']):
                                codeInp5sim2 = data['sms'][0]['code']
                                SMSToLOng5sim2 = "False"
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim2)}/50] Got SMS Code! [Code: {Fore.LIGHTYELLOW_EX}{codeInp5sim2}{Fore.RESET}]")
                                break
                            if count5sim2 == 15:
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim2)}/50] Resend SMS Code...", end="\r")
                            if count5sim2 == 30:
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim2)}/50] Resend SMS Code...", end="\r")
                            if count5sim2 == 51:
                                time.sleep(0.3)
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} SMS code takes to long!{Fore.RESET}", end="\r")
                                SMSToLOng5sim2 = "True"
                                codeInp5sim2 = "1234"
                                break
                            elif (data['status'] == "PENDING"):
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] Phone Number Is Pending...", end="\r")
                                time.sleep(1)
                            elif (data['status'] == "CANCELED"):
                                time.sleep(0.2)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Number is Canceled!{Fore.RESET}")
                                FailedAccValue.value += 1
                                AccGenedValue.value += 1
                                OPAOFAFF = strftime("%H:%M:%S", gmtime())
                                with open("log.txt", "a") as f:
                                    print(f"({OPAOFAFF}) [ERROR] [{threading.currentThread().getName()}] 5sim Number is Canceled!", file=f)
                                if Threads == "1":
                                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                    if RPC_Connect == "True":
                                        try:
                                            rpc.update(
                                                state="[Accounts: " + str(
                                                    AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                                    FailedAccValue.value) + "]",
                                                details="[Status: Generating Account...]",
                                                large_image="logo", large_text="Made By 67")
                                        except:
                                            pass
                                else:
                                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                    if RPC_Connect == "True":
                                        try:
                                            rpc.update(
                                                state="[Accounts: " + str(
                                                    AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                                    FailedAccValue.value) + "]",
                                                details="[Status: Generating Accounts...]",
                                                large_image="logo", large_text="Made By 67")
                                        except:
                                            pass

                                web.close()
                                CancelFiveSImOrder2()
                                time.sleep(4)
                                sys.exit()
                        else:
                            time.sleep(0.2)
                            FailedAccValue.value += 1
                            AccGenedValue.value += 1
                            OPAOFAFF = strftime("%H:%M:%S", gmtime())
                            with open("log.txt", "a") as f:
                                print(f"({OPAOFAFF}) [ERROR] [{threading.currentThread().getName()}] 5sim error!",file=f)
                            if Threads == "1":
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(
                                            state="[Accounts: " + str(
                                                AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                                FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                            large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                            else:
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(
                                            state="[Accounts: " + str(
                                                AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                                FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                            large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                                #  ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Generating Accounts...]" + " {Accounts To Create: " + str(AccGenedValue.value) + "/" + NUMB + " - Accounts Successfully Created: " + str(SuccesAccValue.value) + " - Accounts Failed Created: " + str(FailedAccValue.value) + "}"))
                            time.sleep(0.3)
                            web.close()
                            CancelFiveSImOrder2()
                            sys.exit()

                if SMSService == "smsactivate":
                    scountSMSActivate2 = 1
                    while (scountSMSActivate2 < 51,"https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=getStatus&id=" + idActivate2):
                        url3 = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=getStatus&id=" + idActivate2
                        response3 = requests.get(url=url3)
                        data = response3.text
                        if response3.text == "STATUS_WAIT_CODE":
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(scountSMSActivate2)}/50] Waiting for SMS Code...", end="\r")
                            scountSMSActivate2 = scountSMSActivate2 + 1
                            time.sleep(1)
                            if scountSMSActivate2 == 51:
                                time.sleep(0.3)
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} SMS code takes to long!{Fore.RESET}", end="\r")
                                SMSToLOngActivate = "True"
                                codeInpActivate2 = "1234"
                                break
                            if scountSMSActivate2 == 15:
                                print(end=LINECLEAR)
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(scountSMSActivate2)}/50] Resend SMS Code...", end="\r")
                            if scountSMSActivate2 == 30:
                                print(end=LINECLEAR)
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(scountSMSActivate2)}/50] Resend SMS Code...", end="\r")
                        elif response3.text == "STATUS_WAIT_RETRY":
                            #print("[!] waiting for code clarification...")
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX} [SMS]{Fore.RESET} [{threading.currentThread().getName()}] Waiting for code clarification...", end="\r")
                            time.sleep(1)
                        elif response3.text[0] == "STATUS_OK":
                            SMSToLOngActivate = "False"
                            codeInpActivate2 = data.split(':')
                            codeInpActivate2 = codeInpActivate2[1]
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(scountSMSActivate2)}/50] Got SMS Code! Code: {Fore.LIGHTYELLOW_EX}{codeInpActivate2}{Fore.RESET}")
                            break
                        elif response3.text == "STATUS_CANCEL":
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Order is cancel!{Fore.RESET}", end="\r")
                            FailedAccValue.value += 1
                            AccGenedValue.value += 1

                            if Threads == "1":
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(
                                            state="[Accounts: " + str(
                                                AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                                FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                            large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                            else:
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(
                                            state="[Accounts: " + str(
                                                AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                                FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                            large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                                #  ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Generating Accounts...]" + " {Accounts To Create: " + str(AccGenedValue.value) + "/" + NUMB + " - Accounts Successfully Created: " + str(SuccesAccValue.value) + " - Accounts Failed Created: " + str(FailedAccValue.value) + "}"))
                            time.sleep(4)
                            web.close()
                            sys.exit()
                        else:
                            SMSToLOngActivate = "False"
                            codeInpActivate2 = data.split(':')
                            codeInpActivate2 = codeInpActivate2[1]
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(scountSMSActivate2)}/50] Got SMS Code! Code: {Fore.LIGHTYELLOW_EX}{codeInpActivate2}{Fore.RESET}")
                            break

                if SMSService == "5sim":
                    if SMSToLOng5sim2 == "True":
                        time.sleep(0.2)
                        kfdjsfsf = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"({kfdjsfsf}) [ERROR] [{threading.currentThread().getName()}] 5sim SMS code takes to long!", file=f)
                        back = web.find_element_by_xpath('//*[@id="flow-button-back"]')
                        back.click()
                        time.sleep(0.2)
                        CancelFiveSImOrder2()
                        time.sleep(0.3)
                        PhoneNumberAlreadyUsed()
                    if SMSToLOng5sim2 == "False":
                        pass

                if SMSService == "smsactivate":
                    if SMSToLOngActivate == "True":
                        time.sleep(0.2)
                        TREIR = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"({TREIR}) [ERROR] [{threading.currentThread().getName()}] SMSActivate SMS code takes to long!", file=f)
                        back = web.find_element_by_xpath('//*[@id="flow-button-back"]')
                        back.click()
                        time.sleep(0.2)
                        CancelsOrderActivate2()
                        time.sleep(0.1)
                        PhoneNumberAlreadyUsed()
                    if SMSToLOngActivate == "False":
                        pass
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="field-0"]')))
                send = web.find_element_by_xpath('//*[@id="field-0"]')
                send.click()
                time.sleep(0.2)
                if SMSService == "5sim":
                    send.send_keys(codeInp5sim2)
                if SMSService == "smsactivate":
                    send.send_keys(codeInpActivate2)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.2)
                if SMSService == "5sim":
                    FinishOrder5sim2()
                if SMSService == "smsactivate":
                    FinishOrderSmsActivate2()
                time.sleep(0.6)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/form/div[1]/label')))
                # https://stackoverflow.com/questions/10596417/is-there-a-way-to-get-element-by-xpath-using-javascript-in-selenium-webdriver
                web.execute_script('function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}; getElementByXpath("/html/body/div[1]/div/div[2]/form/div[1]/label").click()')
                time.sleep(0.2)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Battle.net Accept{Fore.LIGHTYELLOW_EX} privacy policy.{Fore.RESET}")
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.2)
                wait = WebDriverWait(web, 200)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-password"]')))
                pswd = web.find_element_by_xpath('//*[@id="capture-password"]')
                pswd.click()
                time.sleep(0.2)
                pswd.send_keys(BattlePass)
                time.sleep(0.2)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Password is set to: {Fore.LIGHTYELLOW_EX}{BattlePass}{Fore.RESET}")
                time.sleep(0.2)
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.2)
                wait = WebDriverWait(web, 200)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
                B0 = web.find_element_by_xpath('//*[@id="capture-battletag"]')
                time.sleep(0.2)
                B0.click()
                B0.clear()
                time.sleep(0.2)
                B0.send_keys(BattleN)
                time.sleep(0.1)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(1)
                if "Value is not allowed" in web.page_source:
                    VALFUADAD = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] BattleNet Tag is Now Allowed!")
                    with open("log.txt", "a") as f:
                        print(f"({VALFUADAD}) [ERROR] [{threading.currentThread().getName()}] BattleNet Tag is Not Allowed!", file=f)
                    time.sleep(0.1)
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Resending BattleNet Tag...", end="\r")
                    BattleN = names.get_last_name()
                    time.sleep(0.1)
                    wait = WebDriverWait(web, 200)
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
                    BN = web.find_element_by_xpath('//*[@id="capture-battletag"]')
                    time.sleep(0.1)
                    BN.click()
                    BN.clear()
                    time.sleep(0.1)
                    BN.send_keys(BattleN)
                    time.sleep(0.2)
                    wait = WebDriverWait(web, 200)
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                    web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                else:
                    pass
                time.sleep(0.3)
                if "Your BattleTag must not contain special characters" in web.page_source:
                    VALUFFDSF = strftime("%H:%M:%S", gmtime())
                    print(F"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} BattleNet Tag can not contain special characters!{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({VALUFFDSF}) [ERROR] [{threading.currentThread().getName()}] BattleNet Tag is Not Allowed! (special characters)", file=f)
                    time.sleep(1)
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Resending BattleNet Tag...", end="\r")
                    BattleN = names.get_last_name()
                    time.sleep(0.3)
                    wait = WebDriverWait(web, 200)
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
                    BN = web.find_element_by_xpath('//*[@id="capture-battletag"]')
                    time.sleep(0.2)
                    BN.click()
                    BN.clear()
                    time.sleep(0.2)
                    BN.send_keys(BattleN)
                    wait = WebDriverWait(web, 200)
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                    web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                    time.sleep(0.2)
                else:
                    pass
                time.sleep(0.8)
                if "Value is not allowed" in web.page_source:
                    VALFUADAD = strftime("%H:%M:%S", gmtime())
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] BattleNet Tag is Now Allowed!")
                    with open("log.txt", "a") as f:
                        print(f"({VALFUADAD}) [ERROR] [{threading.currentThread().getName()}] BattleNet Tag is Not Allowed!", file=f)
                    time.sleep(0.1)
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Resending BattleNet Tag...", end="\r")
                    BattleN = names.get_last_name()
                    time.sleep(0.1)
                    wait = WebDriverWait(web, 200)
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
                    BN = web.find_element_by_xpath('//*[@id="capture-battletag"]')
                    time.sleep(0.1)
                    BN.click()
                    BN.clear()
                    time.sleep(0.1)
                    BN.send_keys(BattleN)
                    time.sleep(0.2)
                    wait = WebDriverWait(web, 200)
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                    web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                    time.sleep(0.2)
                else:
                    pass


                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Battlenet Name is set to: {Fore.LIGHTYELLOW_EX}{BattleN}{Fore.RESET}")
                web.get('https://www.blizzard.com/login')
                time.sleep(0.4)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accountName"]')))
                Nae = web.find_element_by_xpath('//*[@id="accountName"]')
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Battle.net Logging{Fore.RESET} in...")
                time.sleep(0.3)
                Nae.click()
                time.sleep(0.2)
                print(end=LINECLEAR)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: Sending Email Address...", end="\r")
                Nae.send_keys(Email + Domain)
                time.sleep(0.3)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
                time.sleep(0.3)
                PaD = web.find_element_by_xpath('//*[@id="password"]')
                time.sleep(0.2)
                PaD.click()
                time.sleep(0.2)
                print(end=LINECLEAR)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: Sending Password...", end="\r")
                PaD.send_keys(BattlePass)
                time.sleep(0.5)
                web.find_element_by_xpath('//*[@id="submit"]').click()
                time.sleep(1.8)
                if "We couldn't verify your account with that information." in web.page_source:
                    time.sleep(0.2)
                    WHOOPSFD = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"({WHOOPSFD}) [ERROR] [{threading.currentThread().getName()}] Something went wrong!",file=f)
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Something went wrong!{Fore.RESET}")
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    OPAOFAFF = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"({OPAOFAFF}) [ERROR] [{threading.currentThread().getName()}] 5sim error!", file=f)
                    if Threads == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                        #  ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Generating Accounts...]" + " {Accounts To Create: " + str(AccGenedValue.value) + "/" + NUMB + " - Accounts Successfully Created: " + str(SuccesAccValue.value) + " - Accounts Failed Created: " + str(FailedAccValue.value) + "}"))
                    time.sleep(0.3)
                    web.close()
                    time.sleep(0.2)
                    if SMSService == "5sim":
                        CancelFiveSImOrder2()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate2()
                    web.close()
                    time.sleep(2.7)
                    sys.exit()
                else:
                    print(Fore.LIGHTCYAN_EX + "[INFO]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + Fore.LIGHTGREEN_EX + " Battle.net Successfully" + Fore.RESET + " logged in!")

                time.sleep(0.8)
                try:
                    web.find_element_by_xpath('//*[@id="submit"]').click()
                    time.sleep(0.3)
                except WebDriverException:
                    pass

                time.sleep(1)
                try:
                    web.find_element_by_xpath('//*[@id="submit"]').click()
                    time.sleep(0.2)
                except WebDriverException:
                    pass

                web.get('https://account.battle.net/overview')
                print(end=LINECLEAR)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: BattleNet Overview...", end="\r")
                web.get('https://account.battle.net/security#secret-question')
                print(end=LINECLEAR)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: BattleNet Security...", end="\r")
                time.sleep(0.1)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secret-question-card"]/div[2]/div/div[2]/div/div/div[2]/span/a')))
                web.find_element_by_xpath('//*[@id="secret-question-card"]/div[2]/div/div[2]/div/div/div[2]/span/a').click()
                time.sleep(0.2)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="question-select"]')))
                Sec3 = Select(web.find_element_by_xpath('//*[@id="question-select"]'))
                time.sleep(0.2)
                Sec3.select_by_visible_text("Where was the first place you flew?")
                time.sleep(0.2)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Security Question: {Fore.LIGHTYELLOW_EX}Where was the first place you flew?{Fore.RESET}")
                WebDriverWait(web, 200)
                Sec4 = web.find_element_by_xpath('//*[@id="answer"]')
                Sec4.click()
                time.sleep(0.1)
                Sec4.send_keys(SecurityQuestion)
                time.sleep(0.2)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Security Answer: {Fore.LIGHTYELLOW_EX}{SecurityQuestion}{Fore.RESET}")
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sqa-submit"]')))
                web.find_element_by_xpath('//*[@id="sqa-submit"]').click()
                time.sleep(0.1)
                # Chrome end

                # Save account to txt file
                with open("Accounts.txt", "a") as f:
                    print(Email + Domain + ":" + BattlePass + ":" + SecurityQuestion + f" [EMAIL:PASSWORD:SECURITYQUESTION] [AutoSMS:{AutoSMSAcc}] [Country:{Country}]", file=f)

                Discord = config_dictionary["Discord"]
                if Discord != "On" and Discord != "Off":
                    Discord = "Off"
                if Discord == "On":
                    DiscordWebhook = config_dictionary["DiscordWebHook"]
                    time.sleep(0.1)
                    headers = {
                        'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                    }

                    # Sending message
                    # payload = json.dumps({'content': 'test'})
                    try:
                        req = urllib.request.Request(DiscordWebhook, headers=headers)
                        urllib.request.urlopen(req)
                        today = datetime.date.today()
                        alert = {
                            "avatar_url": "https://cdn.discordapp.com/attachments/929415561463599154/934026984298774528/7BQ0TRR1V09W1571358722642.jpg",
                            "name": "Fresh Battle.net Account",
                                "embeds": [
                                {
                                    "author": {
                                        "name": "Fresh Battle.net Account",
                                        "url": "https://discord.gg/fqZZqF43dZ"
                                    },
                                    "description": Email + Domain + ":" + BattlePass + ":" + SecurityQuestion + " ["
                                    "EMAIL:PASSWORD:SECURITYQUESTION] [AutoSMS:True] "f"[Country:{Country}]",
                                    "color": 0x00C7FF,
                                    "thumbnail": {
                                        "url": ""
                                    },
                                    "footer": {
                                        "text": f"{today} - ©NLD Generator"
                                    }
                                }
                            ]
                        }
                        requests.post(DiscordWebhook, json=alert)
                    except Exception as I:
                            AFAFF = strftime("%H:%M:%S", gmtime())
                            with open("log.txt", "a") as f:
                                print(f"({AFAFF}) [ERROR] [{threading.currentThread().getName()}] Error (Discord): {I} ",file=f)
                            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Error (Discord): {I}")

                SuccesAccValue.value += 1
                AccGenedValue.value += 1
                AFAFfdfs = strftime("%H:%M:%S", gmtime())
                with open("log.txt", "a") as f:
                    print(f"({AFAFfdfs}) [SUCCESS] [{threading.currentThread().getName()}] Account is saved in 'Accounts.txt'!",
                        file=f)
                if Threads == "1":
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Account save in {Fore.LIGHTGREEN_EX}Accounts.txt{Fore.RESET}")
                web.close()
                time.sleep(1)
                sys.exit()
            except Exception as BIG2:
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Something went wrong: {Fore.LIGHTRED_EX}{BIG2}{Fore.RESET}")
                FailedAccValue.value += 1
                AccGenedValue.value += 1
                OPAOFAFF = strftime("%H:%M:%S", gmtime())
                with open("log.txt", "a") as f:
                    print(f"({OPAOFAFF}) [ERROR] [{threading.currentThread().getName()}] 5sim error!", file=f)
                if Threads == "1":
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(
                                state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                    FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                large_image="logo", large_text="Made By 67")
                        except:
                            pass
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                    #  ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Generating Accounts...]" + " {Accounts To Create: " + str(AccGenedValue.value) + "/" + NUMB + " - Accounts Successfully Created: " + str(SuccesAccValue.value) + " - Accounts Failed Created: " + str(FailedAccValue.value) + "}"))
                web.close()
                time.sleep(4)
                sys.exit()

        ##########################################################################################################################
        try:
            # First Name
            if FirstName == "":
                FirstName = names.get_first_name(gender='male')
            else:
                FirstName = config_dictionary["FirstName"]
                if FirstName == "Random":
                    FirstName = names.get_first_name(gender='male')
                else:
                    FirstName = config_dictionary["FirstName"]

            # Battle Net Name
            if BattleN == "":
                BattleN = names.get_last_name()
            else:
                BattleN = config_dictionary["BattleNetName"]
                if BattleN == "Random":
                    BattleN = names.get_last_name()
                else:
                    BattleN = config_dictionary["BattleNetName"]

            # Last name
            if LastName == "":
                LastName = names.get_last_name()
            else:
                LastName = config_dictionary["LastName"]
                if LastName == "Random":
                    LastName = names.get_last_name()
                else:
                    LastName = config_dictionary["LastName"]

            # Battle Net Password
            if BattlePass == "":
                BattlePass = random_password_string(length=15, uppercase=True, lowercase=True, numbers=True)
            else:
                BattlePass = config_dictionary["BattleNetPassword"]
                if BattlePass == "Random":
                    BattlePass = random_password_string(length=15, uppercase=True, lowercase=True, numbers=True)
                else:
                    BattlePass = config_dictionary["BattleNetPassword"]

            # cookies
            try:
                web.find_element_by_xpath("//button[@aria-label='Accept cookies']").click()
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Accept Cookies...")
            except:
                time.sleep(0.3)
                pass
            try:
                web.find_element_by_xpath("//button[@aria-label='Accept cookies']").click()
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Accept Cookies...")
            except:
                time.sleep(0.3)
                pass

            BattleNetCountry = config_dictionary["BattleNetCountry"]

            if SMSService == "smsactivate":
                NumbCountrySMSActivate = config_dictionary["smsactivateCountry"]

                if NumbCountrySMSActivate == "2":
                    Country = 'Kazakhstan'
                else:
                    pass
                if NumbCountrySMSActivate == "11":
                    Country = 'Kyrgyzstan'
                else:
                    pass
                if NumbCountrySMSActivate == "163":
                    Country = 'Finland'
                else:
                    pass
                if NumbCountrySMSActivate == "78":
                    Country = 'France'
                else:
                    pass
                if NumbCountrySMSActivate == "43":
                    Country = 'Germany'
                else:
                    pass
                if NumbCountrySMSActivate == "129":
                    Country = 'Greece'
                else:
                    pass
                if NumbCountrySMSActivate == "22":
                    Country = 'India'
                else:
                    pass
                if NumbCountrySMSActivate == "23":
                    Country = 'Ireland'
                else:
                    pass
                if NumbCountrySMSActivate == "13":
                    Country = 'Israel'
                else:
                    pass
                if NumbCountrySMSActivate == "86":
                    Country = 'Italy'
                else:
                    pass
                if NumbCountrySMSActivate == "103":
                    Country = 'Jamaica'
                else:
                    pass
                if NumbCountrySMSActivate == "116":
                    Country = 'Jordan'
                else:
                    pass
                if NumbCountrySMSActivate == "165":
                    Country = 'Luxembourg'
                else:
                    pass
                if NumbCountrySMSActivate == "54":
                    Country = 'Mexico'
                else:
                    pass
                if NumbCountrySMSActivate == "67":
                    Country = 'New Zealand'
                else:
                    pass
                if NumbCountrySMSActivate == "1":
                    Country = 'Ukraine'
                else:
                    pass
                if NumbCountrySMSActivate == "12":
                    Country = 'United States'
                else:
                    pass
                if NumbCountrySMSActivate == "187":
                    Country = 'United States'
                else:
                    pass
                if NumbCountrySMSActivate == "0":
                    Country = 'Russian Federation'
                else:
                    pass

            if SMSService == "5sim":
                NumbCountry5sim = config_dictionary["5simCountry"]

                if NumbCountry5sim == "russia":
                    Country = 'Russian Federation'
                else:
                    pass
                if NumbCountry5sim == "china":
                    Country = "China"
                else:
                    pass
                if NumbCountry5sim == "kyrgyzstan":
                    Country = 'Kyrgyzstan'
                else:
                    pass
                if NumbCountry5sim == "belgium":
                    Country = 'Belgium'
                else:
                    pass
                if NumbCountry5sim == "philippines":
                    Country = 'Philippines'
                else:
                    pass
                if NumbCountry5sim == "canada":
                    Country = 'Canada'
                else:
                        pass
                if NumbCountry5sim == "england":
                    Country = 'United Kingdom'
                else:
                    pass
                    pass
                if NumbCountry5sim == "finland":
                    Country = 'Finland'
                else:
                    pass
                if NumbCountry5sim == "france":
                    Country = 'France'
                else:
                    pass
                if NumbCountry5sim == "germany":
                    Country = 'Germany'
                else:
                    pass
                if NumbCountry5sim == "greece":
                    Country = 'Greece'
                else:
                    pass
                if NumbCountry5sim == "india":
                    Country = 'India'
                else:
                    pass
                if NumbCountry5sim == "ireland":
                    Country = 'Ireland'
                else:
                    pass
                if NumbCountry5sim == "israel":
                    Country = 'Israel'
                else:
                    pass
                if NumbCountry5sim == "italy":
                    Country = 'Italy'
                else:
                    pass
                if NumbCountry5sim == "luxembourg":
                    Country = 'Luxembourg'
                else:
                        pass
                if NumbCountry5sim == "mexico":
                    Country = 'Mexico'
                else:
                    pass
                if NumbCountry5sim == "netherlands":
                    Country = 'Netherlands'
                else:
                    pass
                if NumbCountry5sim == "newzealand":
                    Country = 'New Zealand'
                else:
                    pass
                if NumbCountry5sim == "norway":
                    Country = 'Norway'
                else:
                    pass
                if NumbCountry5sim == "pakistan":
                    Country = 'Pakistan'
                else:
                    pass
                if NumbCountry5sim == "poland":
                    Country = 'Poland'
                else:
                    pass
                if NumbCountry5sim == "turkey":
                    Country = 'Turkey'
                else:
                    pass
                if NumbCountry5sim == "madagascar":
                    Country = 'Madagascar'
                else:
                    pass
                if NumbCountry5sim == "morocco":
                    Country = 'Morocco'
                else:
                    pass
                if NumbCountry5sim == "portugal":
                    Country = 'Portugal'
                else:
                    pass
                if NumbCountry5sim == "romania":
                    Country = 'Romania'
                else:
                    pass
                if NumbCountry5sim == "vietnam":
                    Country = 'Vietnam'
                else:
                    pass
                if NumbCountry5sim == "venezuela":
                    Country = 'Venezuela, Bolivarian Republic Of'
                else:
                    pass
                if NumbCountry5sim == "spain":
                    Country = 'Spain'
                else:
                    pass
                if NumbCountry5sim == "slovakia":
                    Country = 'Slovakia'
                else:
                    pass
                if NumbCountry5sim == "sweden":
                    Country = 'Sweden'
                else:
                    pass
                if NumbCountry5sim == "switzerland":
                    Country = 'Switzerland'
                else:
                    pass
                if NumbCountry5sim == "ukraine":
                    Country = 'Ukraine'
                else:
                    pass
                if NumbCountry5sim == "uruguay":
                    Country = 'Uruguay'
                else:
                    pass
                if NumbCountry5sim == "usa":
                    Country = 'United States'
                else:
                    pass
                if NumbCountry == "uzbekistan":
                    Country = 'Uzbekistan'
                else:
                    pass
            if AutoSMS == "Off":
                Country = BattleNetCountry

            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="capture-country"]')))
            time.sleep(0.2)
            ctr = Select(web.find_element_by_xpath('//*[@id="capture-country"]'))
            time.sleep(0.5)
            ctr.select_by_visible_text(Country)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Country set to: {Fore.LIGHTYELLOW_EX}{Country}{Fore.RESET}")
            time.sleep(5)
            db = web.find_element_by_xpath('//*[@id="dob-field-inactive"]/input[1]')
            db.click()
            db2 = web.find_element_by_xpath('//*[@id="dob-field-active"]/input[1]')
            db2.send_keys(day, month, year)
            time.sleep(0.4)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Date of Birth is set to: {Fore.LIGHTYELLOW_EX}{str(day)} - {str(month)} - {str(year)}{Fore.RESET}")
            time.sleep(1.2)

            Captcha_Service = config_dictionary["CaptchaServiceToUse"]
            NUMB = config_dictionary["Threads"]
            Threads = NUMB

            if Auto_Captcha == "On":
                if Captcha_Service == "2captcha":
                    Get_Website_key_Every_Time = False
                elif Captcha_Service == "AnyCaptcha":
                    Get_Website_key_Every_Time = True
                else:
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Please choose 'AnyCaptcha' or '2captcha'!{Fore.RESET}", end="\r")
                    NUMB = config_dictionary["Threads"]
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    WHOPWHG = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"({WHOPWHG}) [ERROR] [{threading.currentThread().getName()}] Please choose 'AnyCaptcha' or '2captcha'!", file=f)
                    if NUMB == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    web.close()
                    time.sleep(0.3)
                    if AutoSMS == "On":
                        if SMSService == "5sim":
                            CancelsOrder5sim()
                        if SMSService == "smsactivate":
                            CancelsOrderActivate()
                    time.sleep(2.7)
                    sys.exit()
            if CaptchaBypass2 == "On":
                Get_Website_key_Every_Time = False
            if CaptchaBypass2 == "Off" and Auto_Captcha == "Off":
                Get_Website_key_Every_Time = False
            if Get_Website_key_Every_Time == True:
                web.find_element_by_xpath("//*[@id='flow-form-submit-btn']").click()

                # iframe
                wait = WebDriverWait(web, 10)
                iframe_element = wait.until(EC.visibility_of_element_located(
                    (By.XPATH, "//iframe[@class='Z6wXJz-G-6vcu3I0ZoM_B show active lightbox']")))
                web.switch_to.frame(iframe_element)

                time.sleep(3)

                fc_token_element = web.find_element_by_xpath("//*[@name='fc-token']")
                fc_token_element_value = fc_token_element.get_attribute("value")

                # fc_token_element_value = fc_token_element.get_attribute("value")
                ###print("fc-token Element(Order of the values changes when it changes by FunCaptcha or Battle.net): " + str(fc_token_element_value)) #For testing

                # Split value by "|" separator
                fc_token_element_values_list = fc_token_element_value.split('|')

                # Public Key
                fc_token_attribute_pk = fc_token_element_values_list[8]
                fc_token_attribute_pk_list = fc_token_attribute_pk.split("=")
                Blizzard_Website_Key = fc_token_attribute_pk_list[1]

                fc_token_attribute_surl = fc_token_element_values_list[12]
                fc_token_attribute_surl_list = fc_token_attribute_surl.split("=")
                Blizzard_Service_Url = fc_token_attribute_surl_list[1]

                web.switch_to.default_content()
            else:
                # Manual way
                Blizzard_Website_Key = "E8A75615-1CBA-5DFF-8032-D16BCF234E10"
                Blizzard_Service_Url = "https%3A%2F%2Fblizzard-api.arkoselabs.com"

            def Two_Captcha_Solver(Website_Public_Key):
                TwoCaptchaApiKey = config_dictionary["2captchaApiKey"]
                api_key = os.getenv('APIKEY_2CAPTCHA', f'{TwoCaptchaApiKey}')

                solver = TwoCaptcha(api_key)
                print(f"{Fore.LIGHTBLUE_EX}[2CAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] Captcha is{Fore.LIGHTYELLOW_EX} processing{Fore.RESET}")
                try:
                    result = solver.funcaptcha(sitekey=Website_Public_Key, url='https://account.battle.net/creation/flow/creation-full', surl='https://client-api.arkoselabs.com')
                except Exception as n:
                    print(f"{Fore.LIGHTBLUE_EX}[2CAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] 2captcha error: {Fore.LIGHTRED_EX}{str(n)}{Fore.RESET}")
                    NUMB = config_dictionary["Threads"]
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    WHOPWHG = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"({WHOPWHG}) [ERROR] [{threading.currentThread().getName()}] 2captcha error: {n}", file=f)
                    if NUMB == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    web.close()
                    time.sleep(0.3)
                    if AutoSMS == "On":
                        if SMSService == "5sim":
                            CancelsOrder5sim()
                        if SMSService == "smsactivate":
                            CancelsOrderActivate()
                    time.sleep(2.7)
                    sys.exit()

                else:
                    print(f"{Fore.LIGHTBLUE_EX}[2CAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] 2captcha has{Fore.LIGHTGREEN_EX} complete captcha!{Fore.RESET}")
                    Solved_Captcha_Token = str(result["code"])
                    return Solved_Captcha_Token

            def AnyCaptcha_Solver(Api_Key, Website_Public_Key):
                Json_Parameters1 = {
                    "clientKey": Api_Key,
                    "task": {
                        "type": "FunCaptchaTaskProxyless",
                        "websitePublicKey": Website_Public_Key
                    }
                }
                # Post request
                response = requests.post(url="https://api.anycaptcha.com/createTask", json=Json_Parameters1)
                response_json = response.json()
                count5 = 1
                ErrorId = int(response_json['errorId'])
                if ErrorId > 0:
                    CAPTCHD1 = strftime("%H:%M:%S", gmtime())

                    with open("log.txt", "a") as f:
                        print(f"({CAPTCHD1}) [ERROR] [{threading.currentThread().getName()}] Error while Creating Anycaptcha's Task!",file=f)
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTBLUE_EX}[ANYCAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] [0]{Fore.LIGHTRED_EX} Error while Creating AnyCaptcha's Task!{Fore.RESET}", end="\r")
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    if AutoSMS == "On":
                        if SMSService == "5sim":
                            CancelsOrder5sim()
                        if SMSService == "smsactivate":
                            CancelsOrderActivate()
                    web.close()
                    if NUMB == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    time.sleep(3)
                    sys.exit()
                Task_Id = int(response_json["taskId"])
                print(end=LINECLEAR)
                print(Fore.LIGHTBLUE_EX + "[ANYCAPTCHA]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + " [0]" + Fore.LIGHTYELLOW_EX + " Receiving" + Fore.RESET + " AnyCaptcha Task", end="\r")
                Json_Parameters2 = {
                    "clientKey": Api_Key,
                    "taskId": int(Task_Id)
                }
                while True:
                    time.sleep(1.2)
                    response = requests.post(url="https://api.anycaptcha.com/getTaskResult", json=Json_Parameters2)
                    response_json = response.json()

                    # Error
                    ErrorId = int(response_json['errorId'])
                    if ErrorId > 0:
                        CAPTCHD2 = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"({CAPTCHD2}) [ERROR] [{threading.currentThread().getName()}] Captcha: 'ERROR_CAPTCHA_UNSOLVABLE' ",file=f)
                        print(end=LINECLEAR)
                        print(f"{Fore.LIGHTBLUE_EX}[ANYCAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5)}]{Fore.LIGHTRED_EX} Error while getting AnyCaptcha's result token{Fore.RESET}", end="\r")
                        web.close()
                        if AutoSMS == "On":
                            if SMSService == "5sim":
                                CancelsOrder5sim()
                            if SMSService == "smsactivate":
                                CancelsOrderActivate()
                        FailedAccValue.value += 1
                        AccGenedValue.value += 1
                        if NUMB == "1":
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                               large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        else:
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                               large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        time.sleep(3)
                        sys.exit()
                    try:
                        Captcha_status = response_json["status"]
                        if Captcha_status == "ready":
                            Solved_Captcha_Token = str(response_json["solution"]["token"])
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTBLUE_EX}[ANYCAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5)}] AnyCaptcha has {Fore.LIGHTGREEN_EX}complete captcha!{Fore.RESET}")
                            return Solved_Captcha_Token

                        elif Captcha_status == "processing":
                            print(end=LINECLEAR)
                            print(Fore.LIGHTBLUE_EX + "[ANYCAPTCHA]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + " [" + str(count5) + "]" + " Captcha is" + Fore.LIGHTYELLOW_EX + " processing" + Fore.RESET, end="\r")
                            time.sleep(1.2)

                        else:
                            CAPTCHD3 = strftime("%H:%M:%S", gmtime())
                            with open("log.txt", "a") as f:
                                print(f"({CAPTCHD3}) [ERROR] [{threading.currentThread().getName()}] Captcha: 'ERROR_CAPTCHA_UNSOLVABLE' ", file=f)
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTBLUE_EX}[ANYCAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5)}]{Fore.LIGHTRED_EX} Error: ERROR_CAPTCHA_UNSOLVABLE{Fore.RESET}", end="\r")
                            web.close()
                            if AutoSMS == "On":
                                if SMSService == "5sim":
                                    CancelsOrder5sim()
                                if SMSService == "smsactivate":
                                    CancelsOrderActivate()
                            FailedAccValue.value += 1
                            AccGenedValue.value += 1
                            if NUMB == "1":
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(state="[Accounts: " + str(
                                            AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                            FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                                   large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                            else:
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(state="[Accounts: " + str(
                                            AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                            FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                                   large_image="logo", large_text="Made By 67")
                                    except:
                                        pass

                            time.sleep(3)
                            sys.exit()

                    except KeyError:
                        dsfsfksfsgfs = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                                print(f"({dsfsfksfsgfs}) [ERROR] [{threading.currentThread().getName()}] Captcha: 'ERROR_CAPTCHA_UNSOLVABLE' ",file=f)
                        print(end=LINECLEAR)
                        print(f"{Fore.LIGHTBLUE_EX}[ANYCAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5)}]{Fore.LIGHTRED_EX} Error: ERROR_CAPTCHA_UNSOLVABLE{Fore.RESET}", end="\r")
                        print(end=LINECLEAR)
                        web.close()
                        if AutoSMS == "On":
                            if SMSService == "5sim":
                                CancelsOrder5sim()
                            if SMSService == "smsactivate":
                                CancelsOrderActivate()
                        FailedAccValue.value += 1
                        AccGenedValue.value += 1
                        if NUMB == "1":
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                               large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        else:
                            ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                            if RPC_Connect == "True":
                                try:
                                    rpc.update(state="[Accounts: " + str(
                                        AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                               large_image="logo", large_text="Made By 67")
                                except:
                                    pass
                        time.sleep(1.2)
                        sys.exit()
                    count5 = count5 + 1

            # "2Captcha" or "AnyCaptcha" or "AntiCaptcha"
            if Auto_Captcha == "On":
                # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                #  web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.6)
                if Captcha_Service == "AnyCaptcha":
                    Solved_Captcha_Token = AnyCaptcha_Solver(Api_Key=config_dictionary["AnyCaptchaApiKey"],
                                                                 Website_Public_Key=Blizzard_Website_Key)
                elif Captcha_Service == "2captcha":
                    Solved_Captcha_Token = Two_Captcha_Solver(Website_Public_Key=Blizzard_Website_Key)
                else:
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Please choose 'AnyCaptcha' or '2captcha'!{Fore.RESET}")
                    NUMB = config_dictionary["Threads"]
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    WHOPWHG = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"({WHOPWHG}) [ERROR] [{threading.currentThread().getName()}] Please choose 'AnyCaptcha' or '2captcha'!", file=f)
                    if NUMB == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Account...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(
                                    state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(
                                        FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",
                                    large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    web.close()
                    time.sleep(0.3)
                    if AutoSMS == "On":
                        if SMSService == "5sim":
                            CancelsOrder5sim()
                        if SMSService == "smsactivate":
                            CancelsOrderActivate()
                    time.sleep(2.7)
                    sys.exit()

                time.sleep(0.2)
                web.execute_script("document.querySelector('#capture-arkose').value = '" + Solved_Captcha_Token + "'")
                web.execute_script("document.querySelector('#flow-form-submit-btn').disabled=false")
                web.execute_script("document.querySelector('#capture-arkose').click()")
                web.execute_script("document.querySelector('form').submit()")

                time.sleep(0.6)
                    # Captcha End
            else:
                CaptchaBypass = config_dictionary["CaptchaBypass"]
                if CaptchaBypass == "On":
                    web.find_element_by_xpath("//*[@id='flow-form-submit-btn']").click()

                    line = myfile.readline()
                    if line != '':
                        CaptchaToken2 = line.split()
                        CaptchaToken2Real = CaptchaToken2[0]
                        time.sleep(0.3)
                        print(f"{Fore.LIGHTBLUE_EX}[CAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}] Sending{Fore.LIGHTYELLOW_EX} Captcha Token...{Fore.RESET}")
                        web.execute_script("document.querySelector('#capture-arkose').value = '" + CaptchaToken2Real + "'")
                        web.execute_script("document.querySelector('#flow-form-submit-btn').disabled=false")
                        web.execute_script("document.querySelector('#capture-arkose').click()")
                        web.execute_script("document.querySelector('form').submit()")

                    time.sleep(0.3)
                    tempfolder = tempfile.gettempdir()
                    name = 'tokens.txt'
                    completeName = os.path.join(tempfolder, name)
                    with open(completeName, 'r+') as fp:
                        lines = fp.readlines()
                        fp.seek(0)
                        fp.truncate()
                        fp.writelines(lines[1:])
                else:
                    time.sleep(0.8)
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                    web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                    #  print("\rPlease complete captcha..", end="")
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Please complete{Fore.LIGHTYELLOW_EX} Captcha...{Fore.RESET}")
                    wait = WebDriverWait(web, 200)
                    wait.until(EC.element_to_be_clickable((By.ID, 'capture-first-name')))
            try:
                Name = web.find_element_by_xpath('//*[@id="capture-first-name"]')
                Captchadkflf = config_dictionary["CaptchaBypass"]
                if Captchadkflf == "On":
                    print(f"{Fore.LIGHTBLUE_EX}[CAPTCHA]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTGREEN_EX} Valid{Fore.RESET} Captcha Token!")
                time.sleep(0.2)
                Name.send_keys(FirstName)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] First Name is set to: {Fore.LIGHTYELLOW_EX}{FirstName}{Fore.RESET}")
            except NoSuchElementException:
                Threads = config_dictionary["Threads"]
                KMAKNNN = strftime("%H:%M:%S", gmtime())
                FailedAccValue.value += 1
                AccGenedValue.value += 1
                if NUMB == "1":
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass

                with open("log.txt", "a") as f:
                    print(f"({KMAKNNN}) [ERROR] [{threading.currentThread().getName()}] Not valid Captcha Token! ", file=f)
                Captchadkflf = config_dictionary["CaptchaBypass"]
                if Captchadkflf == "On":
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Not Valid Captcha Token! (every Captcha Token You create, can be used within 15 minutes, after 15 minutes, Captcha Token will not work!{Fore.RESET}")
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Make new Captcha Tokens!")
                if Auto_Captcha == "On":
                    if Captcha_Service == "2captcha":
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} 2captcha, not valid Captcha Token{Fore.RESET}", end="\r")
                    if Captcha_Service == "AnyCaptcha":
                        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} AnyCaptcha, not valid Captcha Token{Fore.RESET}", end="\r")
                if AutoSMS == "On":
                    if SMSService == "5sim":
                        CancelsOrder5sim()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate()
                web.close()
                time.sleep(4.5)
                sys.exit()

            lastN = web.find_element_by_xpath('//*[@id="capture-last-name"]')
            lastN.send_keys(LastName)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET } [{threading.currentThread().getName()}] Last Name is set to: {Fore.LIGHTYELLOW_EX}{LastName}{Fore.RESET}")
            web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="capture-email"]')))
            AIM = web.find_element_by_xpath('//*[@id="capture-email"]')
            AIM.send_keys(Email + Domain)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Email is set to: {Fore.LIGHTYELLOW_EX}{Email}{Domain}{Fore.RESET}")
            nmber = web.find_element_by_xpath('//*[@id="capture-phone-number"]')
            nmber.click()
            if AutoSMS == "On":
                if SMSService == "5sim":
                    nmber.send_keys(PhoneNumber5sim)
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] Phone Number is set to: {Fore.LIGHTYELLOW_EX}{PhoneNumber5sim}{Fore.RESET} [Price: {PhonePrice5sim}]")
                if SMSService == "smsactivate":
                    nmber.send_keys(PhoneSMSActivate)
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] Phone Number is set to: {Fore.LIGHTYELLOW_EX}{PhoneSMSActivate}{Fore.RESET} [Price: {PriceSMS}]")
            time.sleep(0.2)
            web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
            time.sleep(1)
            if AutoSMS == "On":
                if SMSService == "smsactivate":
                    SendOrderSMSActivate()
            if "Whoops! Something went wrong." in web.page_source:
                time.sleep(0.2)
                fdsfsdkf = strftime("%H:%M:%S", gmtime())
                with open("log.txt", "a") as f:
                    print(f"({fdsfsdkf}) [ERROR] [{threading.currentThread().getName()}] 'Whoops! Something went wrong.', try switch VPN Connection or switch proxies!", file=f)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} try switch VPN Connection or switch proxies!{Fore.RESET}", end="\r")
                FailedAccValue.value += 1
                AccGenedValue.value += 1
                if NUMB == "1":
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                time.sleep(0.2)
                if AutoSMS == "On":
                    if SMSService == "5sim":
                        CancelsOrder5sim()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate()
                web.close()
                time.sleep(2.7)
                sys.exit()
            else:
                pass

            time.sleep(0.3)
            if "Phone number is already in use" in web.page_source:
                PAIDPAIDFD = strftime("%H:%M:%S", gmtime())
                if NUMB == "1":
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]", large_image="logo",large_text="Made By 67")
                        except:
                            pass
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                if SMSService == "5sim":
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Phone Number Already is been used!{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({PAIDPAIDFD}) [ERROR] [{threading.currentThread().getName()}] 5sim Phone Number already is been used!", file=f)
                if SMSService == "smsactivate":
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Phone Number Already is been used!{Fore.RESET}")
                    with open("log.txt", "a") as f:
                        print(f"({PAIDPAIDFD}) [ERROR] [{threading.currentThread().getName()}] SMSActivate Phone Number already is been used!", file=f)
                time.sleep(0.3)
                if AutoSMS == "On":
                    if SMSService == "5sim":
                        CancelsOrder5sim()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate()
                PhoneNumberAlreadyUsed()
            else:
                pass

            time.sleep(0.3)
            if "Please enter a post-paid phone number." in web.page_source:
                    time.sleep(0.2)
                    NONOFSDF = strftime("%H:%M:%S", gmtime())
                    FailedAccValue.value += 1
                    AccGenedValue.value += 1
                    if NUMB == "1":
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]", large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    else:
                        ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                        if RPC_Connect == "True":
                            try:
                                rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                            except:
                                pass
                    if SMSService == "5sim":
                        print(Fore.LIGHTMAGENTA_EX + "[5SIM]" + Fore.RESET + Fore.LIGHTRED_EX + " Phone number is post-paid!" + Fore.RESET)
                        with open("log.txt", "a") as f:
                            print(f"({NONOFSDF}) [ERROR] [{threading.currentThread().getName()}] Number is post-paid!",
                                file=f)
                    if SMSService == "smsactivate":
                        print(Fore.LIGHTMAGENTA_EX + "[SMS]" + Fore.RESET + Fore.LIGHTRED_EX + " Phone number is "
                        "post-paid!" + Fore.RESET)
                        with open("log.txt", "a") as f:
                            print(f"({NONOFSDF}) [ERROR] [{threading.currentThread().getName()}] Number is post-paid!",
                                  file=f)
                    web.close()
                    time.sleep(0.3)
                    if AutoSMS == "On":
                        if SMSService == "5sim":
                            CancelsOrder5sim()
                        if SMSService == "smsactivate":
                            CancelsOrderActivate()
                    sys.exit()
            else:
                pass
            # Chrome end
            if AutoSMS == "On":
                time.sleep(0.2)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="resend-sms-verification"]')))
                time.sleep(0.3)
                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                if SMSService == "5sim":
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [0/50] Resend SMS Code...",end="\r")
                if SMSService == "smsactivate":
                    print(end=LINECLEAR)
                    print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [0/50] Resend SMS Code...", end="\r")
                time.sleep(1)

                # 5sim
                if SMSService == "5sim":
                    count5sim = 1
                    if phone := 1:
                        codeInp5sim = ""
                    while (count5sim < 51, (requests.get('https://5sim.net/v1/user/check/' + str(id5sim), headers=headers))):
                        response = requests.get('https://5sim.net/v1/user/check/' + str(id5sim), headers=headers)
                        data = json.loads(response.text)
                        if (data['status'] == "RECEIVED"):
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim)}/50] Waiting for SMS Code...",end="\r")
                            count5sim = count5sim + 1
                            time.sleep(1)
                            if (data['sms']):
                                codeInp5sim = data['sms'][0]['code']
                                SMSToLOng5sim = "False"
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim)}/50] Got SMS Code! [Code: {Fore.LIGHTYELLOW_EX}{codeInp5sim}{Fore.RESET}]")
                                break
                            if count5sim == 15:
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim)}/50] Resend SMS Code...", end="\r")
                            if count5sim == 30:
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] [{str(count5sim)}/50] Resend SMS Code...", end="\r")
                            if count5sim  == 51:
                                time.sleep(0.3)
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} SMS code takes to long!{Fore.RESET}", end="\r")
                                SMSToLOng5sim = "True"
                                codeInp5sim = "1234"
                                break
                            elif (data['status'] == "PENDING"):
                                print(end=LINECLEAR)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}] Phone Number Is Pending...", end="\r")
                                time.sleep(2)
                            elif (data['status'] == "CANCELED"):
                                time.sleep(0.2)
                                print(f"{Fore.LIGHTMAGENTA_EX}[5SIM]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Number is Canceled!{Fore.RESET}")
                                FailedAccValue.value += 1
                                AccGenedValue.value += 1
                                OPAOFAFF = strftime("%H:%M:%S", gmtime())
                                with open("log.txt", "a") as f:
                                    print(f"({OPAOFAFF}) [ERROR] [{threading.currentThread().getName()}] 5sim Number is Canceled!",
                                        file=f)
                                if NUMB == "1":
                                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                    if RPC_Connect == "True":
                                        try:
                                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]",large_image="logo", large_text="Made By 67")
                                        except:
                                            pass
                                else:
                                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                    if RPC_Connect == "True":
                                        try:
                                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                                        except:
                                            pass
                                web.close()
                                CancelsOrder5sim()
                                time.sleep(3)
                                sys.exit()
                        else:
                            time.sleep(0.2)
                            FailedAccValue.value += 1
                            AccGenedValue.value += 1
                            OPAOFAFF = strftime("%H:%M:%S", gmtime())
                            with open("log.txt", "a") as f:
                                print(f"({OPAOFAFF}) [ERROR] [{threading.currentThread().getName()}] 5sim error!", file=f)
                            if NUMB == "1":
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]",large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                            else:
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + NUMB + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                            time.sleep(0.3)
                            web.close()
                            CancelsOrder5sim()
                            sys.exit()

                if SMSService == "smsactivate":
                    countSMSActivate = 1
                    while (countSMSActivate < 51,"https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=getStatus&id=" + idActivate):
                        url3 = "https://api.sms-activate.org/stubs/handler_api.php?api_key=" + smsApi + "&action=getStatus&id=" + idActivate
                        response3 = requests.get(url=url3)
                        data = response3.text
                        if response3.text == "STATUS_WAIT_CODE":
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(countSMSActivate)}/50] Waiting for SMS Code...",end="\r")
                            countSMSActivate = countSMSActivate + 1
                            time.sleep(1)
                            if countSMSActivate == 15:
                                print(end=LINECLEAR)
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(countSMSActivate)}/50] Resend SMS Code...", end="\r")
                            if countSMSActivate == 30:
                                print(end=LINECLEAR)
                                web.find_element_by_xpath('//*[@id="resend-sms-verification"]').click()
                                print(Fore.LIGHTMAGENTA_EX + "[SMS]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + " [" + str(countSMSActivate) + "/50]" + " Resend SMS Code...", end="\r")
                            if countSMSActivate == 51:
                                time.sleep(0.3)
                                print(end=LINECLEAR)
                                print(Fore.LIGHTMAGENTA_EX + "[SMS]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + Fore.LIGHTRED_EX + " SMS code takes to long!" + Fore.RESET,end="\r")
                                SMSToLOngActivate = "True"
                                codeInpActivate = "1234"
                                break
                        elif response3.text == "STATUS_WAIT_RETRY":
                            # print("[!] waiting for code clarification...")
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX} [SMS]{Fore.RESET} [{threading.currentThread().getName()}] Waiting for code clarification...", end="\r")
                            time.sleep(1)
                        elif response3.text[0] == "STATUS_OK":
                            SMSToLOngActivate = "False"
                            codeInpActivate2 = data.split(':')
                            codeInpActivate2 = codeInpActivate2[1]
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(countSMSActivate)}/50] Got SMS Code! Code: {Fore.LIGHTYELLOW_EX}{codeInpActivate2}{Fore.RESET}")
                            break
                        elif response3.text == "STATUS_CANCEL":
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Order is cancel!{Fore.RESET}",end="\r")
                            FailedAccValue.value += 1
                            AccGenedValue.value += 1

                            if Threads == "1":
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]",large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                            else:
                                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                                if RPC_Connect == "True":
                                    try:
                                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                                    except:
                                        pass
                                #  ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator" + " [Status: Generating Accounts...]" + " {Accounts To Create: " + str(AccGenedValue.value) + "/" + NUMB + " - Accounts Successfully Created: " + str(SuccesAccValue.value) + " - Accounts Failed Created: " + str(FailedAccValue.value) + "}"))
                            time.sleep(0.3)
                            time.sleep(4)
                            web.close()
                            sys.exit()
                        else:
                            SMSToLOngActivate = "False"
                            codeInpActivate = data.split(':')
                            codeInpActivate = codeInpActivate[1]
                            print(end=LINECLEAR)
                            print(f"{Fore.LIGHTMAGENTA_EX}[SMS]{Fore.RESET} [{threading.currentThread().getName()}] [{str(countSMSActivate)}/50] Got SMS Code! Code: {Fore.LIGHTYELLOW_EX}{codeInpActivate}{Fore.RESET}")
                            break

                if SMSService == "5sim":
                    if SMSToLOng5sim == "True":
                        time.sleep(0.2)
                        TREIR = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"({TREIR}) [ERROR] [{threading.currentThread().getName()}] 5sim SMS code takes to long!", file=f)
                        back = web.find_element_by_xpath('//*[@id="flow-button-back"]')
                        back.click()
                        time.sleep(0.2)
                        CancelsOrder5sim()
                        time.sleep(0.1)
                        PhoneNumberAlreadyUsed()
                    if SMSToLOng5sim == "False":
                        pass
                if SMSService == "smsactivate":
                    if SMSToLOngActivate == "True":
                        time.sleep(0.2)
                        TREIR = strftime("%H:%M:%S", gmtime())
                        with open("log.txt", "a") as f:
                            print(f"({TREIR}) [ERROR] [{threading.currentThread().getName()}] SMSActivate SMS code takes to long!", file=f)
                        back = web.find_element_by_xpath('//*[@id="flow-button-back"]')
                        back.click()
                        time.sleep(0.2)
                        CancelsOrderActivate()
                        time.sleep(0.1)
                        PhoneNumberAlreadyUsed()
                    if SMSToLOngActivate == "False":
                        pass
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="field-0"]')))
                send = web.find_element_by_xpath('//*[@id="field-0"]')
                send.click()
                time.sleep(0.2)
                if SMSService == "5sim":
                    send.send_keys(codeInp5sim)
                if SMSService == "smsactivate":
                    send.send_keys(codeInpActivate)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.2)
                if SMSService == "5sim":
                    FinishOrder5sim()
                if SMSService == "smsactivate":
                    FinishOrderSmsActivate()
                time.sleep(0.3)
            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, 'html/body/div[1]/div/div[2]/form/div[1]/label')))
            #https://stackoverflow.com/questions/10596417/is-there-a-way-to-get-element-by-xpath-using-javascript-in-selenium-webdriver
            web.execute_script('function getElementByXpath(path) {return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}; getElementByXpath("/html/body/div[1]/div/div[2]/form/div[1]/label").click()')
            time.sleep(0.2)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Battle.net Accept{Fore.LIGHTYELLOW_EX} privacy policy.{Fore.RESET}")
            time.sleep(0.1)
            web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
            time.sleep(0.4)
            wait = WebDriverWait(web, 200)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-password"]')))
            time.sleep(0.2)
            pswd = web.find_element_by_xpath('//*[@id="capture-password"]')
            pswd.click()
            time.sleep(0.1)
            pswd.send_keys(BattlePass)
            time.sleep(0.1)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Password is set to: {Fore.LIGHTYELLOW_EX}{BattlePass}{Fore.RESET}")
            time.sleep(0.2)
            web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
            time.sleep(0.2)
            wait = WebDriverWait(web, 200)
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
            B0 = web.find_element_by_xpath('//*[@id="capture-battletag"]')
            time.sleep(0.2)
            B0.click()
            B0.clear()
            time.sleep(0.2)
            # B0.send_keys(BattleN)
            B0.send_keys(BattleN)
            time.sleep(0.2)
            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
            web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
            time.sleep(1.2)
            if "Value is not allowed" in web.page_source:
                VALUFFDSF = strftime("%H:%M:%S", gmtime())
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] BattleNet Tag is Now Allowed!")
                with open("log.txt", "a") as f:
                    print(f"({VALUFFDSF}) [ERROR] [{threading.currentThread().getName()}] BattleNet Tag is Not Allowed!",file=f)
                time.sleep(1)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Resending BattleNet Tag...", end="\r")
                BattleN = names.get_last_name()
                time.sleep(0.3)
                wait = WebDriverWait(web, 200)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
                BN = web.find_element_by_xpath('//*[@id="capture-battletag"]')
                time.sleep(0.2)
                BN.click()
                BN.clear()
                time.sleep(0.2)
                BN.send_keys(BattleN)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.2)
            else:
                pass
            time.sleep(0.3)
            if "Your BattleTag must not contain special characters" in web.page_source:
                VALUFFDSF = strftime("%H:%M:%S", gmtime())
                print(F"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} BattleNet Tag can not contain special characters!{Fore.RESET}")
                with open("log.txt", "a") as f:
                    print(f"({VALUFFDSF}) [ERROR] [{threading.currentThread().getName()}] BattleNet Tag is Not Allowed! (special characters)", file=f)
                time.sleep(1)
                print(end=LINECLEAR)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Resending BattleNet Tag...", end="\r")
                BattleN = names.get_last_name()
                time.sleep(0.3)
                wait = WebDriverWait(web, 200)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
                BN = web.find_element_by_xpath('//*[@id="capture-battletag"]')
                time.sleep(0.2)
                BN.click()
                BN.clear()
                time.sleep(0.2)
                BN.send_keys(BattleN)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.2)
            else:
                pass
            time.sleep(0.9)
            if "Value is not allowed" in web.page_source:
                VALFUADAD = strftime("%H:%M:%S", gmtime())
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] BattleNet Tag is Now Allowed!")
                with open("log.txt", "a") as f:
                    print(f"({VALFUADAD}) [ERROR] [{threading.currentThread().getName()}] BattleNet Tag is Not Allowed!", file=f)
                time.sleep(0.1)
                print(end=LINECLEAR)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Resending BattleNet Tag...", end="\r")
                BattleN = names.get_last_name()
                time.sleep(0.1)
                wait = WebDriverWait(web, 200)
                wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="capture-battletag"]')))
                BN = web.find_element_by_xpath('//*[@id="capture-battletag"]')
                time.sleep(0.1)
                BN.click()
                BN.clear()
                time.sleep(0.1)
                BN.send_keys(BattleN)
                time.sleep(0.2)
                wait = WebDriverWait(web, 200)
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]')))
                web.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
                time.sleep(0.2)
            else:
                pass
            print(Fore.LIGHTCYAN_EX + "[INFO]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + " BattleNet Name is set to: " + Fore.LIGHTYELLOW_EX + BattleN + Fore.RESET)
            web.get('https://www.blizzard.com/login')
            time.sleep(0.5)
            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accountName"]')))
            Nae = web.find_element_by_xpath('//*[@id="accountName"]')
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTYELLOW_EX} Battle.net Logging{Fore.RESET} in...")
            time.sleep(0.4)
            Nae.click()
            time.sleep(0.4)
            print(end=LINECLEAR)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: Sending Email Address...", end="\r")
            Nae.send_keys(Email + Domain)
            time.sleep(0.4)
            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
            PaD = web.find_element_by_xpath('//*[@id="password"]')
            time.sleep(0.2)
            PaD.click()
            time.sleep(0.2)
            print(end=LINECLEAR)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: Sending Password...", end="\r")
            PaD.send_keys(BattlePass)
            time.sleep(0.6)
            web.find_element_by_xpath('//*[@id="submit"]').click()
            time.sleep(1.8)
            if "We couldn't verify your account with that information." in web.page_source:
                time.sleep(0.2)
                WHOOPSFD = strftime("%H:%M:%S", gmtime())
                with open("log.txt", "a") as f:
                    print(f"({WHOOPSFD}) [ERROR] [{threading.currentThread().getName()}] Something went wrong!", file=f)
                print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Something went wrong!{Fore.RESET}")
                FailedAccValue.value += 1
                AccGenedValue.value += 1
                if Threads == "1":
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]", large_image="logo",large_text="Made By 67")
                        except:
                            pass
                else:
                    ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                    if RPC_Connect == "True":
                        try:
                            rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]",large_image="logo", large_text="Made By 67")
                        except:
                            pass
                time.sleep(0.2)
                if AutoSMS == "On":
                    if SMSService == "5sim":
                        CancelsOrder5sim()
                    if SMSService == "smsactivate":
                        CancelsOrderActivate()
                web.close()
                time.sleep(2.7)
                sys.exit()
            else:
                print(Fore.LIGHTCYAN_EX + "[INFO]" + Fore.RESET + " [" + threading.currentThread().getName() + "]" + Fore.LIGHTGREEN_EX + " Battle.net Successfully" + Fore.RESET + " logged in!")
            try:
                web.find_element_by_xpath('//*[@id="submit"]').click()
                time.sleep(0.2)
            except WebDriverException:
                pass
            time.sleep(1)
            try:
                web.find_element_by_xpath('//*[@id="submit"]').click()
                time.sleep(0.2)
            except WebDriverException:
                pass
            time.sleep(0.1)
            web.get('https://account.battle.net/overview')
            print(end=LINECLEAR)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: BattleNet Overview...", end="\r")
            web.get('https://account.battle.net/security#secret-question')
            print(end=LINECLEAR)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Status: BattleNet Security...", end="\r")
            time.sleep(0.1)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="secret-question-card"]/div[2]/div/div[2]/div/div/div[2]/span/a')))
            web.find_element_by_xpath('//*[@id="secret-question-card"]/div[2]/div/div[2]/div/div/div[2]/span/a').click()
            time.sleep(0.4)
            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="question-select"]')))
            Sec3 = Select(web.find_element_by_xpath('//*[@id="question-select"]'))
            time.sleep(0.2)
            Sec3.select_by_visible_text("Where was the first place you flew?")
            time.sleep(0.2)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Security Question: {Fore.LIGHTYELLOW_EX}Where was the first place you flew?{Fore.RESET}")
            WebDriverWait(web, 200)
            Sec4 = web.find_element_by_xpath('//*[@id="answer"]')
            Sec4.click()
            time.sleep(0.1)
            Sec4.send_keys(SecurityQuestion)
            time.sleep(0.2)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Security Answer: {Fore.LIGHTYELLOW_EX}{SecurityQuestion}{Fore.RESET}")
            wait = WebDriverWait(web, 200)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sqa-submit"]')))
            web.find_element_by_xpath('//*[@id="sqa-submit"]').click()
            time.sleep(0.1)

            if AutoSMS == "On":
                AutoSMSAcc = True
            elif AutoSMS == "Off":
                AutoSMSAcc = False

            with open("Accounts.txt", "a") as f:
                print(Email + Domain + ":" + BattlePass + ":" + SecurityQuestion + f" [EMAIL:PASSWORD:SECURITYQUESTION] [AutoSMS:{AutoSMSAcc}] [Country:{Country}]", file=f)

            Discord = config_dictionary["Discord"]
            if Discord != "On" and Discord != "Off":
                Discord = "Off"
            if Discord == "On":
                DiscordWebhook = config_dictionary["DiscordWebHook"]
                time.sleep(0.1)
                headers = {
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
                }

                # Sending message
                # payload = json.dumps({'content': 'test'})
                try:
                    req = urllib.request.Request(DiscordWebhook, headers=headers)
                    urllib.request.urlopen(req)
                    today = datetime.date.today()
                    alert = {
                        "avatar_url": "https://cdn.discordapp.com/attachments/929415561463599154/934026984298774528/7BQ0TRR1V09W1571358722642.jpg",
                        "name": "Fresh Battle.net Account",
                        "embeds": [
                            {
                                "author": {
                                    "name": "Fresh Battle.net Account",
                                    "url": "https://discord.gg/fqZZqF43dZ"
                                },
                                "description": Email + Domain + ":" + BattlePass + ":" + SecurityQuestion + f" [EMAIL:PASSWORD:SECURITYQUESTION] [AutoSMS:{AutoSMSAcc}] [Country:{Country}]",
                                "color": 0x00C7FF,
                                "thumbnail": {
                                    "url": ""
                                },
                                "footer": {
                                    "text": f"{today} - ©NLD Generator"
                                }
                            }
                        ]
                    }
                    requests.post(DiscordWebhook, json=alert)
                except Exception as I:
                    AFAFF = strftime("%H:%M:%S", gmtime())
                    with open("log.txt", "a") as f:
                        print(f"({AFAFF}) [ERROR] [{threading.currentThread().getName()}] Error (Discord): {I} ", file=f)
                    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Error (Discord): {I}")

            SuccesAccValue.value += 1
            AccGenedValue.value += 1
            Threadf = config_dictionary["Threads"]
            AFAFfdfs = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"({AFAFfdfs}) [SUCCESS] [{threading.currentThread().getName()}] Account is saved in 'Accounts.txt'!", file=f)
            if Threads == "1":
                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                if RPC_Connect == "True":
                    try:
                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]", large_image="logo",large_text="Made By 67")
                    except:
                        pass
            else:
                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                if RPC_Connect == "True":
                    try:
                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]", large_image="logo", large_text="Made By 67")
                    except:
                        pass
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Account save in {Fore.LIGHTGREEN_EX}Accounts.txt{Fore.RESET}")
            web.close()
            time.sleep(0.2)
            sys.exit()

        except Exception as BIG1:
            FailedAccValue.value += 1
            AccGenedValue.value += 1
            KXUOGAF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"({KXUOGAF}) [ERROR] [{threading.currentThread().getName()}] Something went wrong: {BIG1}", file=f)
            if Threads == "1":
                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Account...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                if RPC_Connect == "True":
                    try:
                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Account...]", large_image="logo",large_text="Made By 67")
                    except:
                        pass
            else:
                ctypes.windll.kernel32.SetConsoleTitleW("NLD v2.6 Generator [Status: Generating Accounts...] {Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Good: " + str(SuccesAccValue.value) + " - Failed: " + str(FailedAccValue.value) + "}")
                if RPC_Connect == "True":
                    try:
                        rpc.update(state="[Accounts: " + str(AccGenedValue.value) + "/" + Threads + " - Failed: " + str(FailedAccValue.value) + "]", details="[Status: Generating Accounts...]", large_image="logo",large_text="Made By 67")
                    except:
                        pass

            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}] Something went wrong: {Fore.LIGHTRED_EX}{BIG1}{Fore.RESET}")
            web.close()
            time.sleep(3)
            sys.exit()

    class ProxyRotatorClass:
        def __init__(self, proxies):
            self.proxies = proxies
            self.last_proxy_index = -1
            self.l = Lock()

        def Get_Proxy_Old(self):
            with self.l:
                index = self.last_proxy_index + 1
                if index >= len(self.proxies):
                    index = 0
                self.last_proxy_index = index
                return self.proxies[index]

        def Get_Proxy(self):
            with self.l:
                return random.choice(self.proxies)


    def Get_Proxy_List(Proxy_File_Path):
        with open(Proxy_File_Path) as file:
            file_content = file.read()
            proxies_list = file_content.split("\n")
            return proxies_list


    # Threads
    if __name__ == "__main__":
        try:
            LINECLEAR = '\x1b[2K'
            Accounts_To_Make = get_user_inputs()

            SuccesAccValue = Value('i', 0)

            AccGenedValue = Value('i', 0)

            FailedAccValue = Value('i', 0)

            with open('settings.json') as file:
                config_dictionary = json.load(file)
            try:
                tempfolder = tempfile.gettempdir()
                name = 'tokens.txt'
                completeName = os.path.join(tempfolder, name)
                myfile = open(completeName, 'r')  # ***Opened file at the begining***
                # Use Proxy if "On"
            except:
                pass

            if config_dictionary["UseProxy"] == "On":

                Proxies_List = Get_Proxy_List(Proxy_File_Path="proxies.txt")
                ProxyRotator = ProxyRotatorClass(Proxies_List)
                Locking_Thing_For_Proxy = Lock()
                # Start threads
                threads_objects = []
                for i in range(Accounts_To_Make):
                    A_Proxy = ProxyRotator.Get_Proxy()
                    t = threading.Thread(target=Account_Generator, args=(A_Proxy, Locking_Thing_For_Proxy,))
                    t.start()
                    time.sleep(2)
                    threads_objects.append(t)

            else:

                # Start threads
                threads_objects = []
                for i in range(Accounts_To_Make):
                    t = threading.Thread(target=Account_Generator, args=(None,))
                    t.start()
                    time.sleep(0.4)
                    threads_objects.append(t)

            # Wait for all threads to complete
            for each_item_thread_object in threads_objects:
                each_item_thread_object.join()
        except Exception as BIAF:
            KXUOGAF = strftime("%H:%M:%S", gmtime())
            with open("log.txt", "a") as f:
                print(f"({KXUOGAF}) [ERROR] [{threading.currentThread().getName()}] Something went wrong: {BIAF}", file=f)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Something went wrong: {BIAF}{Fore.RESET}")
            time.sleep(3)
            sys.exit()

    NUMBERS = config_dictionary["Threads"]
    fdsafsdfsdkf = strftime("%H:%M:%S", gmtime())
    with open("log.txt", "a") as f:
        print(f"({fdsafsdfsdkf}) [STATS] Accounts: {NUMBERS}/{str(AccGenedValue.value)} - Good: {str(SuccesAccValue.value)} - Failed: {str(FailedAccValue.value)}",  file=f)

    FINIFJDSFSDF = strftime("%H:%M:%S", gmtime())
    with open("log.txt", "a") as f:
        print(f"(End time: {FINIFJDSFSDF})", file=f)
except Exception as TEST:
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} [{threading.currentThread().getName()}]{Fore.LIGHTRED_EX} Something went wrong: {TEST}{Fore.RESET}")
    time.sleep(3)
    sys.exit()