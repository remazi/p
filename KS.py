import requests
import uuid
import sys
import os
import pyfiglet
from random import *
import colorama 
from colorama import *
import time 
import string 
from user_agent import generate_user_agent
import random
import pyfiglet
# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[1;32m' #اخضر
A = '\033[2;34m'#ازرق داكن
C = '\033[1;35m' #وردي
B = '\033[1;36m'#سمائي
Y = '\033[1;34m' #ازرق

# = = = = = = = = = = = =
print (" ❖❀～ 𝐑  ࿖ ～❀❖ ")
banner = C
print(F+banner)
no = '1234567890'
abc = 'QAZWSXEDCRFVTGBYHNUJMIKLOP'
po = '_.'
ua = '1234567890'
an = '1234567890QAZWSXEDCRFVTGBYHNUJMIKOLP'
BGreen='\033[1;32m'
BRed ='\033[1;31m'
kwgd = input(F+"""\n
[1] E6.44 / حرف + ارقام
[2] EE.00 / حرفين + رقمين
[3] EEE.0 / ثلاث احرف + رقم
[4] EA.EA / 
[5] EB.NN / حرفين عشوائيات + حرفين مكررين
[6] EB.BB / حرف عشوائي + ثلاث احرف مكررين
[7] T.T.D
[8] NOTE / اختارها واقراهن
= = = = = = 
[~] CHOISE ONE » """)
pp = '5'
id = '5012751368'
tt = '5332779790:AAF1VfauHnzQnkEs5qDolLTEzNwON4fsSHY'
print()
ru = ('{"account_created": false, "errors": {"email": [{"message": "Too many accounts are using a@gmail.com.", "code": "email_sharing_limit"}], "__all__": [{"message": "Create a password at least 6 characters long.", "code": "too_short_password"}]}, "dryrun_passed": false, "username_suggestions": [], "status": "ok", "error_type": "form_validation_error"}')
def G():    
    if kwgd =='1':
        number = 0
        kumber = 0
        while True:
            t = random.choice(abc)
            k = random.choice(no)
            aa = random.choice(po)
            s = random.choice(ua)
            us = t + s + aa + k + k         
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade,data=data).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')                
if kwgd == "2":
    number = 0
    kumber = 0
    while True:
            t = random.choice(abc)
            k = random.choice(no)
            j = random.choice(po)
            us = t + t + j + k + k    
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade,data=data).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n☆ يـوزر انـسـتـا مـمـيـز ✅\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝑇𝐸𝐿𝐸 : @FX205 | @T_X_6')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                
if kwgd == "3":
	number = 0
	kumber = 0
	while True:
            t = random.choice(abc)
            p = random.choice(no)
            a = random.choice(po)
            us = t + t + t + a + p   
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                
if kwgd == "4":
    number = 0
    kumber = 0
    while True:
            t = random.choice(abc)
            p = random.choice(an)
            a = random.choice(po)
            us = t + p + a + t + p 
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
if kwgd == "6":
    number = 0
    kumber = 0
    while True:
            u = str("".join(random.choice(abc)for i in range(1)))
            k = random.choice(abc)
            j = random.choice(po)
            us = u + k + j + k + k
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')          
                
if kwgd == "5":
    number = 0
    kumber = 0
    while True:
            u = str("".join(random.choice(abc)for i in range(2)))
            k = random.choice(abc)
            j = random.choice(po)
            us = u + j + k + k
            url = 'https://www.instagram.com/accounts/web_create_ajax/attempt/'
            heade_ruks={
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8,ar-SA;q=0.7',
                'content-length': '61',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': 'ig_cb=2; ig_did=BB52B198-B05A-424E-BA07-B15F3D4C3893; mid=YAlcaQALAAHzmX6nvD8dWMRVYFCO; shbid=15012; rur=PRN; shbts=1612894029.7666144; csrftoken=CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/emailsignup/',
                'sec-ch-ua': '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
                'x-csrftoken': 'CPKow8myeXW9AuB3Lny0wNxx0EzoDQoI',
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0Plwj5om112fwzrrYnMNjMLPnyWfFFq1tG7MCcMv5_vN9M',
                'x-instagram-ajax': '72bda6b1d047',
                'x-requested-with': 'XMLHttpRequest'

            } 
#The data shown above are identical Do not touch anything developer Ruks          
            data_ruks={
                'email' : 'a@gmail.com',
                'username': f'{us}',
                'first_name': 'AA',
                'opt_into_one_tap': 'false'
            }
            da = requests.post(url,headers=heade_ruks,data=data_ruks).text
            if ru in  da:
                kumber+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
                with open('insta.txt', 'a') as x:
                	x.write(us+ '\n')
                	tlg =(f'https://api.telegram.org/bot{tt}/sendMessage?chat_id={id}&text=\n NEW USER\n━━━━━━━━❪❂❫━━━━━━━━\n- 𝚄𝚂𝙴𝚁 : ( {us} )')           	
                	req = requests.post(tlg)             
                
            else:
                number+=1
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{banner}\n [=] Hit : {kumber} \n [=] Bad : {number}\n [=] Block : 0\n [=] {us} ",end='')
G()       
if kwgd == "7":
	print (Z+'    @HDDDDH     ')
if kwgd == "8":
	print ('    @RWKKK / ادخل هنا ضروري    ')