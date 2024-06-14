# Use this script to find various accounts existence of a given username

import requests
from colorama import init, Fore, Back, Style

init(autoreset=True)

class OSINT:
    def OSINTTool(self, username):
        websites = {
            "Instagram" : "https://instagram.com/",
            "Github" : "https://github.com/",
            "Facebook" : "https://facebook.com/",
            "TryHackMe" : "https://tryhackme.com/p/",
            "LeetCode" : "https://leetcode.com/u/",
            "Twitter / X" : "https://x.com/"
        }


        for key, value in websites.items():
            req = requests.get(value + username)
            
            if req.status_code == 200:
                print(Fore.GREEN + f'Account Found : {key} : {value + username}')
                
            elif req.status_code == 404:
                print(Fore.RED + f"404 Account Not Found : {key}")
                
            else:
                print(Fore.BLUE + f"Error finding account on {key} : Status Code : {req.status_code}")
                
request = OSINT()

username = input("Enter the username to be examined : ")
request.OSINTTool(username)
