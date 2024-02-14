import requests,os,sys
import re
from time import sleep
import random

luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;96m"
xnhac = "\033[1;36m"
trang='\033[1;37m'
ndp_tool = trang + "~" + trang + "[" + do + "+" + trang + "] " + trang + "=> "
ndp = trang + "~" + trang + "[" + do + "÷" + trang + "] " + trang + "=> "
# Config
__SHOP__ = 'ShopDucPhat.Tk'
__ZALO__ = '0396.735.565'
__ADMIN__ = 'Trần Ngọc Anh'
__FACEBOOK__ = 'techsavy04'
__VERSION__ = '1.0'
d='  '*5
#List Config
ListBody=[]
def starttool():
	
	a=f'''{hong}
	
	
 
   {d}     _______  .---..-.   .-.{xduong}04{hong}
    {d}    |__   __|( .-._)\ \ / /   
   {d}       )| |  (_) \    \ V /    
    {d}     (_) |  _  \ \    ) /     
     {d}      | | ( `-'  )  (_)      
  {d}       `-'  `----'            
                          
\033[1;37m~ \033[1;32m Bắt Đầu Vào Tool 
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
{ndp_tool}\033[1;31mCopyright By: \033[1;35m{__ADMIN__}
{ndp_tool}\033[1;32mZalo: \033[1;34m{__ZALO__}
{ndp_tool}\033[1;36mFacebook: \033[1;37mFb.com/{__FACEBOOK__}
{ndp_tool}\033[0;93mTool Spam Messenger Version {__VERSION__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	'''
	return a
def bandef():
	
	a=f'''{hong}
	
	
 
   {d}     _______  .---..-.   .-.{xduong}04{hong}
    {d}    |__   __|( .-._)\ \ / /   
   {d}       )| |  (_) \    \ V /    
    {d}     (_) |  _  \ \    ) /     
     {d}      | | ( `-'  )  (_)      
  {d}       `-'  `----'            
                          
\033[1;37m~ \033[1;32m Liên Hệ:  \033[0;93m Fb.com/techsavy04 \033[1;37m~ \033[1;32m để mua key vip
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
{ndp_tool}\033[1;31mCopyright By: \033[1;35m{__ADMIN__}
{ndp_tool}\033[1;32mZalo: \033[1;34m{__ZALO__}
{ndp_tool}\033[1;36mFacebook: \033[1;37mFb.com/{__FACEBOOK__}
{ndp_tool}\033[0;93mTool Spam Messenger Version {__VERSION__}
\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
	'''
	return a
def GetName(headers):
    Data = requests.get("https://mbasic.facebook.com", headers=headers)
    if 'Đăng xuất' in Data.text:
        name = str(re.findall('id="mbasic_logout_button">.*?<', Data.text)[0]).replace(' ', '').replace(
            'id="mbasic_logout_button">Đăngxuất(', '').replace(')<', '')
        return name
    else:
        return "Cookie Die"


def SendMess(UrlListTinNhan, cookie, headers,ListBody):
    Tinnhan = requests.get(UrlListTinNhan, headers=headers).text
    
    body=random.choice(ListBody)
    Name=re.findall('<title.*?</title>', Tinnhan)[0].replace('<title>', '').replace('</title>', '')
    
    UrlSend = re.findall('action="/messages/send?.*?"', Tinnhan)[0].replace('"', '').replace('amp;', '').replace(
        'action=', '')
    fb_dtsg = Tinnhan.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
    jazoest = Tinnhan.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
    tids = Tinnhan.split('<input type="hidden" name="tids" value="')[1].split('"')[0]
    id = tids.split(':')[0].replace('cid.c.', '')
    csid = re.findall('input type="hidden" name="csid" value=".*?"', Tinnhan)[0].replace(
        'input type="hidden" name="csid" value="', '').replace('"', '')
    data = (
        f"fb_dtsg={fb_dtsg}&jazoest={jazoest}&body={body}&send=G%E1%BB%ADi&tids={tids}&wwwupp=C3&ids[{id}]={id}&referrer=&ctype=&cver=legacy&csid={csid}")
    hd = {
        'authority': 'mbasic.facebook.com',
        'method': 'POST',
        'path': UrlSend,
        'secheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'cache-control': 'max-age=0',
        'content-length': '303',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie,
        'origin': 'https://mbasic.facebook.com',
        'referer': 'https://mbasic.facebook.com' + UrlSend,
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    }
    b = requests.post('https://mbasic.facebook.com' + UrlSend, data=data, headers=hd)
    if b.status_code == 200:
        return Name,'1',body
    else:
        return Name,'0',body


# vao tool#
os.system("clear")

logo=bandef()
for i in range(len(logo)):
     sys.stdout.write(logo[i])
     sys.stdout.flush()
     sleep(0.007)
print()
Cookie= str(input(ndp_tool+luc+'Nhập Cookie Facebook '+trang+': '+vang))
print()
TnDem = int(input(ndp_tool+luc+'Nhập Số Lần Gửi Tin Nhắn'+trang+': '+vang))
CountTn = int(input(ndp_tool+luc+'Vui Lòng Nhập Số Tin Nhắn Bạn Muốn Gửi'+trang+': '+vang))
for i in range(CountTn):
	TinNhan=str(input(f'{ndp_tool} {luc} Nhập Tin Nhắn {i+1} {trang}: {vang}'))
	ListBody.append(TinNhan)
print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


cookie = 'datr=yV3IZT_rGoGQpMR8OViN6TVx;sb=yV3IZYYx6hbZFS9sug_b70FG;ps_l=0;ps_n=0;c_user=100089801793694;xs=18%3Aod8DOxDS9RQeoA%3A2%3A1707630101%3A-1%3A6283;fr=03bPLnDxMPdsrMa5T.AWV6tRSgGRtT1C7eEsFDXUAWf4c.BlyF4Q..AAA.0.0.BlyF4Q.AWWH0btmgLs;m_page_voice=100089801793694;'

UrlHome = 'https://mbasic.facebook.com/home'
headers = {
    'authority': 'mbasic.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
    'origin': 'https://mbasic.facebook.com',

    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'viewport-width': '1186',
    'x-fb-friendly-name': 'storiesUpdateSeenStateMutation',
    'x-fb-lsd': 'YCCQAywyZyd74odVp6QBrw',
    'cookie': cookie
}
ad = GetName(headers)
if ad == "Cookie Die":
    exit(do + "Cookie Die Vui Lòng Lấy Lại Code !!!")
else:
    print(do + " Facebook" + trang + ' ==> ' + vang + '[ ' + luc + ad + vang + " ]")
DataHome = requests.get(UrlHome, headers=headers).text
UrlTinNhan = 'https://mbasic.facebook.com' + re.findall('"/messages/?.*?"', DataHome)[0].replace('"', '').replace(
    'amp;', '')
DataTinNhan = requests.get(UrlTinNhan, headers=headers).text
UrlListTinNhans = re.findall('"/messages/read?.*?"', DataTinNhan)

for i in range(len(UrlListTinNhans)):
    UrlListTinNhan = 'https://mbasic.facebook.com' + re.findall('"/messages/read?.*?"', DataTinNhan)[i].replace('"',
                                                                                                                '').replace(
        'amp;', '')
    Tinnhan = requests.get(UrlListTinNhan, headers=headers).text
    Name = re.findall('<title.*?</title>', Tinnhan)[0].replace('<title>', '').replace('</title>', '')
    print(f'{vang}[ {hong}{i + 1}{vang} ] {do}=> {xnhac}{Name}')
print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
try:
    dem = int(input(f'{vang}Nhập đoạn chát muốn spam: '))
except:
    exit(do + "Vui Lòng Nhập Đúng Định Dạng !!!")
UrlListTinNhan = 'https://mbasic.facebook.com' + re.findall('"/messages/read?.*?"', DataTinNhan)[dem - 1].replace('"',
                                                                                                                  '').replace(
    'amp;', '')
print('\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

for i in range(TnDem):
	Name,Status,body= SendMess(UrlListTinNhan, cookie, headers,ListBody)
	if Status == "1":
	   print(f'{vang}[ {do}{i+1}{vang}  {hong}{Name} {trang}| {xduong}{body} {trang} | {luc} success ')
	   sleep(7)
	else:
		print('Thất bại')
