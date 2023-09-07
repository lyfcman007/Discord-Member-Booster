"""
                   Not allowed to resell or use to generate income. 
   If found, we will not be able to proceed From software developers ( GENIX SHOP )
            Thank you for accepting the terms of use of this software.
"""

import random,time
import datetime
import threading,os
import json

try:
	from capmonster_python import HCaptchaTask
	import requests
except ImportError:
	os.system("pip install capmonster_python")
	os.system("pip install requests")

done = 0
bad = 0

def headers_reg():
	response1 = requests.get("https://discord.com")
	cookie = response1.cookies.get_dict()
	cookie['locale'] = "us"
	__dcfduid = cookie['__dcfduid']
	__sdcfduid = cookie['__sdcfduid']
	__cfruid = cookie['__cfruid']
	headers = {
	       "accept": "*/*",
	       "authority": "discord.com",
	       "method": "POST",
	       "path": "/api/v9/auth/register",
	       "scheme": "https",
	       "origin": "discord.com",
	       "referer": "discord.com/register",
	       "x-debug-options": "bugReporterEnabled",
	       "accept-language": "en-US,en;q=0.9",
	       "connection": "keep-alive",
	       "content-Type": "application/json",
	       "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
	       "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
	       "sec-fetch-dest": "empty",
	       "sec-fetch-mode": "cors",
	       "sec-fetch-site": "same-origin",
	       "cookie": f"__dcfduid={__dcfduid};__sdcfduid={__sdcfduid};_gcl_au=1.1.112584149.1686070530;OptanonConsent=isIABGlobal=false&datestamp=Tue+Jun+06+2023+23%3A55%3A30+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2FADJqYCUD&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1;_ga=GA1.1.1610756780.1686070537;_ga_Q149DFWHT7=GS1.1.1686070536.1.0.1686070539.0.0.0;__cf_bm=btpRH4vTOEcwikDHB0QBu404QuPhOivnK86ngimpulA-1686711134-0-ATfCY3ZxHGCsLUjU9HVNEX3RRk45FFeLwMkv5r21pc1VyYri80f0okPZqwv5f9aPDA==;__cfruid={__cfruid}"
	}
	return headers
	
    
def request_fingerprint():
	response2 = requests.get("https://discordapp.com/api/v9/experiments", headers=headers_reg()).json()
	fingerprint = response2["fingerprint"]
	return fingerprint

def createAccounts():
	global done
	global bad
	#resp = requests.get("https://raw.githubusercontent.com/TahaGorme/100k-usernames/main/usernames.txt").text
	username = "GENIX SHOP"
	fileproxy = open("proxies.txt", "r").read().splitlines()
	prox = random.choice(fileproxy)
	proxy = f"http://{prox}"
	retry_time = datetime.datetime.now()
	hidden = retry_time.strftime("%H:%M:%S")
	
	param = {
		"http": proxy,
		"https": proxy
	}
	
	try:
		resp = requests.get("https://google.com",proxies=param,timeout=15)
		
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mProtocol HTTP(s) - {prox}\x1b[00m")
		sitekey = "4c672d35-0701-42b2-88c3-78380b0db560"
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mCAPTCHA Solver - \x1b[36m{sitekey[:18]}*****\x1b[00m")
		f = open("config.json")
		config = json.load(f)
		capmonster = HCaptchaTask(config['captcha_key'])
		task_id = capmonster.create_task("https://discord.com/register", sitekey)
		result = capmonster.join_task_result(task_id)
		hcaptcha = result.get("gRecaptchaResponse")
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mCAPTCHA Solved !\x1b[00m")
		numberand = random.randint(1000,9999)
		email = f"genixshop_booster{numberand}@gmail.com"
		
		target = "https://discord.com/api/v9/auth/register"
		response = requests.post(target,headers=headers_reg(),json={"fingerprint":request_fingerprint(),"email":email,"username":username,"password":"As257400","invite":config['invite_code'],"consent":'true',"date_of_birth":"2000-06-05","gift_code_sku_id":'null',"captcha_key":hcaptcha,"promotional_email_opt_in":'true'},proxies=param, allow_redirects=True,timeout=10)
		if (response.status_code == 400):
			bad += 1
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			if "captcha" in response.json():
				print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mCAPTCHA cannot be solved !\x1b[00m")
				createAccounts()
			else:
				print(response.json())
				# createAccounts()
		elif (response.status_code == 201 or response.status_code == 200 or response.status_code == 204):
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			done += 1
			tokens = response.json()['token']
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[35m{tokens[:22]}****** \x1b[31m| \x1b[32mJoined round - {done}\x1b[00m")
		elif (response.status_code == 429):
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			retry_after = response.json()['retry_after']
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mWait \x1b[31mRalteLimited {retry_after}s !\x1b[00m")
			time.sleep(float(retry_after))
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mWait \x1b[35mRateLimited Successfully !\x1b[31m")
			createAccounts()
		else:
			bad += 1
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mError Don't know server: \x1b[31m")
			print(response.json(),response)
			createAccounts()
	except:
		retry_time = datetime.datetime.now()
		hidden = retry_time.strftime("%H:%M:%S")
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[34mProtocol Raw !\x1b[00m")
		sitekey = "4c672d35-0701-42b2-88c3-78380b0db560"
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mCAPTCHA Solver - \x1b[36m{sitekey[:18]}*****\x1b[00m")
		f = open("config.json")
		config = json.load(f)
		capmonster = HCaptchaTask(config['captcha_key'])
		task_id = capmonster.create_task("https://discord.com/register", sitekey)
		result = capmonster.join_task_result(task_id)
		hcaptcha = result.get("gRecaptchaResponse")
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mCAPTCHA Solved !\x1b[00m")
		numberand = random.randint(1000,9999)
		email = f"genixshop_booster{numberand}@gmail.com"
		
		target = "https://discord.com/api/v9/auth/register"
		response = requests.post(target,headers=headers_reg(),json={"fingerprint":request_fingerprint(),"email":email,"username":username,"password":"As257400","invite":config['invite_code'],"consent":'true',"date_of_birth":"2000-06-05","gift_code_sku_id":'null',"captcha_key":hcaptcha,"promotional_email_opt_in":'true'},allow_redirects=True,timeout=10)
		if (response.status_code == 400):
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			bad += 1
			if "captcha" in response.json():
				print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mCAPTCHA cannot be solved !\x1b[00m")
				createAccounts()
			else:
				print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mError Don't know server: \x1b[31m")
				print(response.json(),response)
				createAccounts()
		elif (response.status_code == 201 or response.status_code == 200 or response.status_code == 204):
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			done += 1
			tokens = response.json()['token']
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[35m{tokens[:22]}****** \x1b[31m| \x1b[32mJoined round - {done}\x1b[00m")
		elif (response.status_code == 429):
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			retry_after = response.json()['retry_after']
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mWait \x1b[31mRalteLimited {retry_after}s !\x1b[00m")
			time.sleep(float(retry_after))
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mWait \x1b[35mRateLimited Successfully !\x1b[31m")
			createAccounts()
		else:
			bad += 1
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mError Don't know server: \x1b[31m")
			print(response.json(),response)
			createAccounts()
	
		
	
			
	

ban_check = """\x1b[32m
       ╔══╦═╦═╦╦══╦╗╔╗╔══╦╗╔╦═╦═╗
       ║╔═╣╦╣║║╠║║╩╗╔╝║══╣╚╝║║║╬║
       ║╚╗║╩╣║║╠║║╦╝╚╗╠══║╔╗║║║╔╝
       ╚══╩═╩╩═╩══╩╝╚╝╚══╩╝╚╩═╩╝ 1.2.0\x1b[00m
"""

def createBooster():
	f = open("config.json")
	config = json.load(f)
	os.system("clear")
	print(ban_check)
	invite = config['invite_code']
	print(f"       \x1b[34m> \x1b[32mJoin to `\x1b[31mhttps://discord.gg/{invite}\x1b[32m`")
	print()
	
	for th in range(config['threads']):
		createAccounts()
	
	print("\n")
	print(f"        \x1b[00m[END] --> Good: {done} | Error: {bad}")
	print()
	os.system("rm -rf proxies.txt")


def info():
	f = open("config.json")
	config = json.load(f)
	os.system("clear")
	print(ban_check)
	invite = config['invite_code']
	print(f"       \x1b[34m> \x1b[32mJoin to `\x1b[31mhttps://discord.gg/{invite}\x1b[32m`")
	print()
	input("    \x1b[36mPLEASE ENTER TO ENJOYS....")
	createBooster()
	

retry_time = datetime.datetime.now()
hidden = retry_time.strftime("%H:%M:%S")


def capmonster_check(key):
	resp = requests.post("https://api.capmonster.cloud/getBalance",json={"clientKey": key}).json()
	if resp['errorId'] == 1:
		retry_time = datetime.datetime.now()
		hidden = retry_time.strftime("%H:%M:%S")
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mCapmonster Not available !\x1b[00m")
	else:
		if resp['balance'] == 0:
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mCapmonster not enough for use !\x1b[00m")
		else:
			retry_time = datetime.datetime.now()
			hidden = retry_time.strftime("%H:%M:%S")
			print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[32mSuccessfully !\x1b[00m")
			time.sleep(1)
			info()

def getproxy():
	resp = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all").text
	with open("proxies.txt", "w+") as client:
		client.write(resp)

os.system("clear")
print(ban_check)
getproxy()
try:
	file = open("config.json")
	config = json.load(file)
	
	if config['captcha_key'] == "":
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mCaptcha key is None !\x1b[00m")
	else:
		print(f"   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[34mChecking DataBase...\x1b[00m")
		capmonster_check(config['captcha_key'])
except FileNotFoundError:
	print(f"""   \x1b[33m[\x1b[36mINFO - {hidden}\x1b[33m] : \x1b[31mFileNotFoundError 'config.json'\x1b[00m """)

