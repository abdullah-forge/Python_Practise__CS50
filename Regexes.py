#Phone Number validator

import re
numbers = ["0300-1234567", "+92-345-9876543", 
           "00923111234567", "0333 1234567", 
           "042-99201145"]

print("Valid Numbers")
for number in numbers:
    if re.search(r"^(0|\+92-)3\d{2}-\d{7}$", number):
        print(number)
    
    else:
        print("Invalid Number")
        print(number)

#URL Extractor

import re 
email_body = "Please update your password at https://secure-login.com. Do not visit http://sketchy-site.org/login or www.fake-bank.net!"
urls = []

if match := re.findall(r"(?:https?://|www\.)[\w./-]+",email_body, re.IGNORECASE):
    urls.extend(match)

print("All emails in the email body")
for url in urls:
    print(url)

#Data cleaning basic
import re
messy_log = "Error_Code: 404!@# System_Temp: 85°C... Rebooting now???"

if match := re.sub(r"[!@#.?]+", "", messy_log):
    print(match)

# color hex code checker

import re

color_codes = ["#BF00FF", "#8A2BE2", "ElectricPurple", "#123", "#GHIJKL", "#000000", "#1234567"]
codes = []

print("Valid UI Colors:")
for color in color_codes:
    if match := re.search(r"^#[0-9a-f]{6}$",color, re.IGNORECASE):
        codes.append(match.group())
        #print(match)

for code in codes:
    print(code)
