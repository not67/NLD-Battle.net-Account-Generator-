# imports
from twocaptcha import TwoCaptcha
from anticaptchaofficial.funcaptchaproxyless import *
import requests
import time
import sys
import colorama
colorama.init(autoreset=False)
from colorama import Fore, Back, Style
# End inports


def TwoCaptcha_Solver(Api_Key, Website_Public_Key, Page_Url, Service_Url):
    # https://github.com/2captcha/2captcha-python/blob/master/examples/funcaptcha.py

    solver = TwoCaptcha(Api_Key)
    print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + " Captcha is" + Fore.LIGHTYELLOW_EX + " processing" + Fore.RESET)
    try:
        result = solver.funcaptcha(sitekey=Website_Public_Key,
                                   url=Page_Url,
                                   surl=Service_Url)
    except Exception as e:
        print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTRED_EX +  " Error while getting 2Captcha result" + Fore.RESET)
        print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTRED_EX + str(e) + Fore.RESET)
        time.sleep(3.0)
        sys.exit(e)
    else:
        print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + " 2Captcha has" + Fore.LIGHTGREEN_EX + " complete captcha!" + Fore.RESET)
        return result




def AnyCaptcha_Solver(Api_Key, Website_Public_Key):

        # Task
        #print(Fore.LIGHTMAGENTA_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTYELLOW_EX + " Creating" + Fore.RESET + " AnyCaptcha Task")
        #print()
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

        # Error check
        ErrorId = int(response_json['errorId'])
        if ErrorId > 0:
            print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTRED_EX + " Error while Creating AnyCaptcha's Task!" + Fore.RESET)
            raise Exception(str(response_json))

        # ID
        Task_Id = int(response_json["taskId"])

        # Loop
        print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTYELLOW_EX + " Receiving" + Fore.RESET + " AnyCaptcha Task")
        Json_Parameters2 = {
            "clientKey": Api_Key,
            "taskId": int(Task_Id)
        }

        while True:
            time.sleep(2)
            response = requests.post(url="https://api.anycaptcha.com/getTaskResult", json=Json_Parameters2)
            response_json = response.json()

            # Error
            ErrorId = int(response_json['errorId'])
            if ErrorId > 0:
                print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTRED_EX + " Error while getting AnyCaptcha's result token" + Fore.RESET)
    #            raise Exception(str(response_json))

            # Status
            Captcha_status = response_json["status"]
            if Captcha_status == "ready":
                Solved_Captcha_Token = str(response_json["solution"]["token"])
                print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + " AnyCaptcha has" + Fore.LIGHTGREEN_EX +  " complete captcha!" + Fore.RESET)
                return Solved_Captcha_Token
                break #This line is not needed

            elif Captcha_status == "processing":
                print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + " Captcha is" + Fore.LIGHTYELLOW_EX + " processing" + Fore.RESET)
                pass

            else:
                print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTRED_EX +  " Error while getting AnyCaptcha's result" + Fore.RESET)
             #   raise Exception(str(response_json))



def Anti_Captcha_Solver(Api_Key, Page_Url, Website_Public_Key):
    # https://github.com/AdminAnticaptcha/anticaptcha-python
    # https://github.com/AdminAnticaptcha/anticaptcha-python/blob/master/funcaptcha_proxyless_example.py

    solver = funcaptchaProxyless()
    solver.set_verbose(1)
    solver.set_key(Api_Key)
    solver.set_website_url(Page_Url)
    solver.set_website_key(Website_Public_Key)

    token = solver.solve_and_return_solution()
    if token != 0:
        print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + " AntiCaptcha has" + Fore.LIGHTGREEN_EX + " complete captcha!" + Fore.RESET)
        #print("[CAPTCHA]" "AntiCaptcha has solved the Captcha, Result token: " + token)
        return str(token)
    else:
        print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTRED_EX + " task finished with error " + solver.error_code + Fore.RESET)
        print(Fore.LIGHTBLUE_EX + "[CAPTCHA]" + Fore.RESET + Fore.LIGHTRED_EX + " Anti Captcha Error: " + str(solver.error_code) + Fore.RESET)
        raise Exception(str(solver.error_code))