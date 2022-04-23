import ctypes
import hashlib
import sys
from threading import Thread
import tempfile
from selenium.webdriver.common.proxy import *

from urllib.request import urlopen, Request
import json
import wget
from seleniumwire import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from seleniumwire.undetected_chromedriver import ChromeOptions
from keyauth2 import api
from readsettings import ReadSettings
import colorama
colorama.init(autoreset=False)
from colorama import Fore, Style
from pathlib import Path
from time import gmtime, strftime
import random
from pypresence import Presence

start = strftime("%H:%M:%S", gmtime())

def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
        path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return


ctypes.windll.kernel32.SetConsoleTitleW("NLD v1.1 Captcha Token Generator")


keyauthapp = api("", "", "", "", hash_to_check=None)  # ("your application name", "your owner id", "your application secret","version")


def slow_type(text, speed, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()


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

try:
    with open('settings.json') as file:
        config_dictionary = json.load(file)
    LicenseKey = config_dictionary["LicenseKey"]
except Exception as FS:
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Something Went wrong: {FS}")
    time.sleep(3)
    sys.exit()

Logo = """╔╗╔╦  ╔╦╗  ╔═╗┌─┐┌─┐┌┬┐┌─┐┬ ┬┌─┐  ╔╦╗┌─┐┬┌─┌─┐┌┐┌  ╔═╗┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
║║║║   ║║  ║  ├─┤├─┘ │ │  ├─┤├─┤   ║ │ │├┴┐├┤ │││  ║ ╦├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
╝╚╝╩═╝═╩╝  ╚═╝┴ ┴┴   ┴ └─┘┴ ┴┴ ┴   ╩ └─┘┴ ┴└─┘┘└┘  ╚═╝└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─"""
slow_type(f"{Logo}", 0.00001)
time.sleep(0.5)
slow_type(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Verify License Key... / Connecting to Discord RPC...", 0.04)
try:
    rpc = Presence("950684234996129812")
    rpc.connect()
    rpc.update(details="[Status: Logging In...]", large_image="battlenet", large_text="Made By 67")
    RPC_Connect = "True"
except Exception as E:
    time.sleep(1)
    RPC_Connect = "False"
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Couldn't connect to Discord RPC! [{E}]{Fore.RESET}")
keyauthapp.license(LicenseKey)
if RPC_Connect == "True":
    rpc.update(details="[Status: Successfully Logged In!]", large_image="battlenet", large_text="Made By 67")
ctypes.windll.kernel32.SetConsoleTitleW("NLD v1.1 Captcha Token Generator")
time.sleep(0.9)

cls()
time.sleep(0.4)

try:
    config = ReadSettings("settings.json")
    ThreadingOpjects = config["Threads"]
except Exception as F:
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Something Went wrong: {F}")
    time.sleep(3)
    sys.exit()
try:
    tempfolder = tempfile.gettempdir()
    name = 'tokens.txt'
    name2 = 'unknown.txt'
    name3 = 'backup.txt'
    completeName = os.path.join(tempfolder, name)
    completeName2 = os.path.join(tempfolder, name2)
    completeName3 = os.path.join(tempfolder, name3)
    file1 = open(completeName, 'r')
    Lines = file1.readlines()
    file2 = open(completeName2, 'r')
    Lines2 = file2.readlines()
    num_lines = sum(1 for line in open(completeName))
except:
    pass

try:
    KALA = open(completeName2, 'r+')
    KALA.truncate(0)
    dfdsff = open(completeName3, 'r+')
    dfdsff.truncate(0)
except:
    pass
user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
    'Mozilla/5.0 (X11; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0'
    'Mozilla/5.0 (Windows NT 10.0; rv:87.0) Gecko/20100101 Firefox/81.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/90.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/91.0'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/81.0',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
]


#print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTYELLOW_EX} Note: {Fore.RESET}When you are using the Captcha Token Generator,{Fore.LIGHTRED_EX} DON'T use a vpn{Fore.RESET}, it will make the Captcha only{Fore.LIGHTYELLOW_EX} harder{Fore.RESET}.\nSo please {Fore.LIGHTYELLOW_EX}TURN OFF{Fore.RESET} your vpn if it is On!")
if ThreadingOpjects == "1":
    if RPC_Connect == "True":
        rpc.update(state="[Captcha Tokens: 0/" + ThreadingOpjects + "]", details="[Status: Generating Token...]", large_image="battlenet", large_text="Made By 67")
else:
    if RPC_Connect == "True":
        rpc.update(state="[Captcha Tokens: 0/" + ThreadingOpjects + "]", details="[Status: Generating Tokens...]", large_image="battlenet", large_text="Made By 67")

print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Captcha Token(s) will be {Fore.LIGHTYELLOW_EX}only{Fore.RESET} working for {Fore.LIGHTYELLOW_EX}15 minutes!{Fore.RESET}")
time.sleep(3)

def SeleniumWire():
    tempfolder = tempfile.gettempdir()
    TempSele = '.seleniumwire'
    SeleniumFolder = os.path.join(tempfolder, TempSele)
    selenium_ca = SeleniumFolder + 'seleniumwire-ca.pem'
    time.sleep(0.3)
    dirMake = os.path.join(SeleniumFolder)
    if not os.path.exists(dirMake):
        time.sleep(0.8)
        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Installing requirements...")
        os.mkdir(dirMake)
        time.sleep(0.1)
        # seleniumwire-ca.pem
        wget.download('https://onedrive.live.com/download?cid=71AF184AC7C76CB1&resid=71AF184AC7C76CB1%21101356&authkey=AALORNwuTn_Muas', out=SeleniumFolder)
        print()
        # seleniumwire-dhparam.pem
        wget.download('https://onedrive.live.com/download?cid=71AF184AC7C76CB1&resid=71AF184AC7C76CB1%21101357&authkey=AM7v7OOvJBDboqk', out=SeleniumFolder)
        time.sleep(0.8)
        cls()

dfskfsf = os.path.join(completeName)

if Path(completeName).is_file():
    if num_lines >= 1:
        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Do you want to delete the previous Captcha Tokens [Found: {Fore.LIGHTYELLOW_EX}{num_lines}{Fore.RESET}]? (yes or no)")
        pAnsDelete = input("- Your Answer: ")
        if pAnsDelete == "yes":
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTYELLOW_EX} Deleting{Fore.RESET} Captcha Token(s)...")
            KALA = open(completeName, 'r+')
            KALA.truncate(0)
            time.sleep(0.4)
        elif pAnsDelete == "no":
            pass
        elif pAnsDelete == "":
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} I said: {Fore.LIGHTRED_EX}yes or no{Fore.RESET}!")
            time.sleep(3)
            sys.exit()
        elif pAnsDelete != "":
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} I said: {Fore.LIGHTRED_EX}yes or no{Fore.RESET}!")
            time.sleep(3)
            sys.exit()
    else:
        pass
else:
    pass
print(f"{Fore.LIGHTBLUE_EX}[PROXY]{Fore.RESET} Do you want to use proxies (this ensures that your ip will not get blacklist and\nyou can generate a lot more tokens on your home ip) (yes or no)")
anser_proxies = input("- Your Answer: ")
if anser_proxies == "yes":
    Using_Proxies = True
elif anser_proxies == "no":
    Using_Proxies = False
    pass
elif anser_proxies == "":
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} I said: {Fore.LIGHTRED_EX}yes or no{Fore.RESET}!")
    time.sleep(3)
    sys.exit()
elif anser_proxies != "":
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} I said: {Fore.LIGHTRED_EX}yes or no{Fore.RESET}!")
    time.sleep(3)
    sys.exit()

def ChromeDriver():
    driver_google = 'chromedriver.exe'
    complete_temp_chromedriver = os.path.join(tempfolder, driver_google)
    if Path(complete_temp_chromedriver).is_file():
        pass
    else:
        wget.download('https://onedrive.live.com/download?cid=71AF184AC7C76CB1&resid=71AF184AC7C76CB1%21101352&authkey=AGBN1p5H3ebmAFo', out=complete_temp_chromedriver)

def func(number):
    #  while True:
    if Using_Proxies == True:
        try:
            lines_proxies = open('proxies.txt').read().splitlines()
            random_proxy_line = random.choice(lines_proxies)
            print(f"{Fore.LIGHTBLUE_EX}[PROXY]{Fore.RESET} Using proxy: {Fore.LIGHTYELLOW_EX}{random_proxy_line}{Fore.RESET}")
        except Exception as prx:
            time.sleep(0.2)
            print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Something went wrong: {prx}{Fore.RESET}")
            time.sleep(4)
            with open(completeName2, "w") as f:
                f.writelines("True")
            sys.exit()
    try:

        Random_User_Agent = random.choice(user_agent)
        url = "https://account.battle.net/creation/flow/creation-full"
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:loggingPrefs'] = {'performance': 'INFO'}

    except Exception as F:
        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Something Went wrong: {F}")
        time.sleep(3)
        sys.exit()
    countToken = 1

    def interceptor(request):
        del request.headers['accept']
        del request.headers['accept-encoding']
        del request.headers['connection']
        #del request.headers['accept-language']
        del request.headers['content-type']
        del request.headers['user-agent']

        request.headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        request.headers['accept-encoding'] = 'gzip, deflate, br'
        request.headers['connection'] = 'keep-alive'
        #request.headers['accept-language'] = 'en-US;q=0.8,en;q=0.7'
        request.headers['content-type'] = 'application/x-www-form-urlencoded'
        request.headers['user-agent'] = f'{Random_User_Agent}'
        if (request.url == "https://account.battle.net/creation/flow/creation-full/step/get-started"):
            response = request.body.decode('utf-8')
            splitted = response.split('name="arkose"\r\n\r\n')
            token = splitted[1].split('|')
            link = splitted[1].split('\r')
            CaptchaToken = link[0]
            request.abort()
            with open(completeName, "a") as f:
                print(f"{CaptchaToken}", file=f)
            with open(completeName3, "a") as f:
                print(f"{CaptchaToken}", file=f)
          #  print(f"{Fore.LIGHTBLUE_EX}[CAPTCHA]{Fore.RESET}{Fore.LIGHTYELLOW_EX} Token{Fore.LIGHTGREEN_EX} saved!{Fore.RESET}")
            time.sleep(0.3)
            browser.close()
    try:
        Chrome_Options = ChromeOptions()

        headless_proxy = "http://127.0.0.1:3128"
        seleniumwire_options = {
            "proxy": {"http": headless_proxy, "https": headless_proxy, "no_proxy": ""}
        }
        Chrome_Options.add_experimental_option('excludeSwitches', ['enable-logging'])
        Chrome_Options.add_argument(f'user-agent={Random_User_Agent}')
        Chrome_Options.add_argument("--window-size=350,600")
       # Chrome_Options.add_argument("--proxy-server=localhost:8087")
        if Using_Proxies == True:
            set_seleniumwire_options = {
                'proxy': {
                    'http': f'http://{random_proxy_line}',
                    'https': f'https://{random_proxy_line}',
                    'no_proxy': 'localhost,127.0.0.1',

                },
                'exclude_hosts': ['https://blizzard-api.arkoselabs.com']
            }
            browser = webdriver.Chrome(options=Chrome_Options, desired_capabilities=capabilities, seleniumwire_options=set_seleniumwire_options)
        else:
            browser = webdriver.Chrome(options=Chrome_Options, desired_capabilities=capabilities)
        browser.request_interceptor = interceptor
        browser.get(url)
        time.sleep(1)
    except Exception as Chrome:
        time.sleep(0.2)
        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET}{Fore.LIGHTRED_EX} Something went wrong: {Chrome}{Fore.RESET}")
        time.sleep(4)
        with open(completeName2, "w") as f:
            f.writelines("True")
        sys.exit()
   # agent = browser.execute_script("return navigator.userAgent")
  #  print(agent)
    if "Too many attempts." in browser.page_source:
        print(f"{Fore.LIGHTCYAN_EX}[INFO] {Fore.RESET}{Fore.LIGHTRED_EX}To Manny Attempts... {Fore.RESET}[Means you have Generate to MUCH Captcha Tokens, so please try later again!]")
        browser.close()
        time.sleep(4)
        with open(completeName2, "w") as f:
            f.writelines("True")
        sys.exit()
    else:
        with open(completeName2, "w") as f:
            f.writelines("False")
    # for request in browser.requests:
    #    print(request.response.headers)
    try:
        browser.find_element_by_xpath("//button[@aria-label='Accept cookies']").click()
    except:
        time.sleep(0.6)
        pass
    try:
        browser.find_element_by_xpath("//button[@aria-label='Accept cookies']").click()
    except:
        time.sleep(0.6)
        pass
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="flow-form-submit-btn"]'))).click()
  #  browser.find_element_by_xpath('//*[@id="flow-form-submit-btn"]').click()
    # first get all lines from file

# input("")


Threads = ThreadingOpjects

number_of_threads = int(Threads)

buttons = []

threads = []

for number in range(number_of_threads):
    t = Thread(target=func, args=(number,))
    t.start()
    time.sleep(2)
    threads.append(t)
    buttons.append(False)
for t in threads:
    t.join()
try:
    tempfolder = tempfile.gettempdir()
    name = 'tokens.txt'
    name2 = 'unknown.txt'
    completeName = os.path.join(tempfolder, name)
    completeName2 = os.path.join(tempfolder, name2)
    file1 = open(completeName, 'r')
    Lines = file1.readlines()
    file2 = open(completeName2, 'r')
    Linesfdf = file2.readlines()
    num_lines = sum(1 for line in open(completeName))
except Exception as i:
    pass
try:
    file2 = open(completeName2, 'r')
    Linesfdf = file2.readlines()
    IfELse = Linesfdf[0]
except:
    pass

def Loop():
    while True:
        with open(completeName3, 'r') as file_captcha:
            lines_captcha_file = len(file_captcha.readlines())
        print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Captcha Tokens: {Fore.LIGHTYELLOW_EX}{lines_captcha_file}/{str(number_of_threads)}{Fore.RESET}",end="\r")
        if ThreadingOpjects == "1":
            if RPC_Connect == "True":
                rpc.update(state="[Captcha Tokens: "+str(lines_captcha_file)+"/" + ThreadingOpjects + "]",details="[Status: Generating Token...]", large_image="battlenet", large_text="Made By 67")
        else:
            if RPC_Connect == "True":
                rpc.update(
                    state="[Captcha Tokens: " + str(lines_captcha_file) + "/" + ThreadingOpjects + "]",details="[Status: Generating Tokens...]", large_image="battlenet", large_text="Made By 67")
        time.sleep(1)
        CompleteThreads = number_of_threads - 1
        if lines_captcha_file > CompleteThreads:
            break
if IfELse == "False":
    file2 = open(completeName3, 'w')
    Loop()
    time.sleep(0.6)
    print()
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Press {Fore.LIGHTYELLOW_EX}'Ctrl + C'{Fore.RESET} to exit...")
else:
    print(f"{Fore.LIGHTCYAN_EX}[INFO]{Fore.RESET} Press {Fore.LIGHTYELLOW_EX}'Ctrl + C'{Fore.RESET} to exit...")