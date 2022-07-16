#/usr/bin/python
#.......................................
#       (seener or viewer tool)
#.......................................
import os
try:
    system = os.system('whoami')
    if system == '0':
        try:
            os.system('clear')
        except:
            os.system('cls')
        print ('\n:D [termux]\n')
    elif 'u0_' in system:
        os.system('clear')
        print ('\n:D [termux] or [pyroid]\n')
    elif 'root' in system or 'kali' in system:
        os.system('clear')
        print ('\n:D [linux]\n')
    else:
        print ('\nsystem not recognizable\n')
except:
    try:
        os.system ('clear')
    except:
        os.system ('cls')
    print ('\n:D [windows-c.m.d.]\n')
# ......... import ......... 
import time,random
try:
    import requests
except importError:
    os.system('pip install requests')
    import requests
try:
    import pyuseragents
except importError:
    os.system ('pip install pyuseragents')
    import pyuseragents
try:
    import datetime
except importError:
    os.system ('pip install datetime')
    import datetime
try:
    os.system('clear')
except:
    os.system('cls')
print ('\033[20;0036m')
try:
    os.system ('date')
except:
    pass
time.sleep(1.5)
print ('''\n\033[95m<<< \033[91mviewer \033[92m[U.R.L.]\033[95m >>>\n''')
print ('\t\033[31m[*] \033[34m|version 1.0.0|\n')
time.sleep(0.5)
#................
'''
\033[20;37mmethods:

\033[20;37m┌─\033[31m[\033[92mtelegram\033[31m]\033[20;37m—|    |─\033[31m[\033[92mall-url\033[31m]\033[20;37m─|
\033[20;37m└──╼ \033[31m[\033[92m1\033[31m]\033[20;37m ─╼╼─|      |─────\033[31m[\033[92m0\033[31m]\033[20;37m───|
|                               |

\033[20;37m┌─\033[31m[\033[92mm.youtube.com\033[31m]\033[20;37m—|  |─\033[31m[\033[92mmyoutube.be\033[31m]\033[20;37m─|
└──╼ \033[31m[\033[92m2\033[31m]\033[20;37m ─╼╼────|       |──────\033[31m[\033[92m3\033[31m]\033[20;37m───|
|                                |
\033[20;37m┌─\033[31m[\033[92maparat\033[31m]\033[20;37m—|     |─\033[31m[\033[92mpro-url\033[31m]\033[20;37m─||
└──-\033[31m [\033[92m4\033[31m]\033[20;37m ─╼╼─|  |─────\033[31m[\033[92m5\033[31m]\033[20;37m───|

\033[35m[~] \033[36mtype number here\t\033[31m_> \033[0m'''
#....................
method = input ('''\033[20;37m
_____________________________________________
|>>  ||||||||||||||||||||||||||||||||||||  <<|
|>>  ____________________________________  <<|
|>>  |———\033[31m[\033[92mtelegram\033[31m]\033[20;37m———|  |——\033[31m[\033[92mm.youtube\033[31m]\033[20;37m—|  <<|
|>>  |______\033[31m[\033[92m1\033[31m]\033[20;37m_______|  |______\033[31m[\033[92m2\033[31m]\033[20;37m_____|  <<|
|>>  |                |  |              |  <<|
|>>  |——\033[31m[\033[92myoutube.be\033[31m]\033[20;37m——|  |—\033[31m[\033[92maparat.com\033[31m]\033[20;37m—|  <<|
|>>  |______\033[31m[\033[92m3\033[31m]\033[20;37m_______|  |______\033[31m[\033[92m4\033[31m]\033[20;37m_____|  <<|
|>>  |                |  |              |  <<|
|>>  |———\033[31m[\033[92mall-url\033[31m]\033[20;37m————|  |———\033[31m[\033[92mpro-url\033[31m]\033[20;37m——|  <<|
|>>  |______\033[31m[\033[92m5\033[31m]\033[20;37m_______|  |______\033[31m[\033[92m6\033[31m]\033[20;37m_____|  <<|
|>>  ————————————————————————————————————  <<|
|>>  ||||||||||||||||||||||||||||||||||||  <<|
—————————————————————————————————————————————
\033[31m[!]>> \033[35mEXIT\033[93m: \033[91;37m[99]

\033[35m[~] \033[36mtype number method\033[35m [#]> \033[0m''')
if method == '99':
    quit()
time.sleep(0.5)
proxi:str = input('\n\033[35m[?] \033[36mproxy address _> \033[20;37m')
url:str = input('\n\033[35m[?] \033[36murl \033[35m[https://t.me/cd_home/1] \033[36m_> \033[20;37m')
data:str = ''
print('\n')
date = (datetime.datetime.today())
print (f'\n\033[31m[*] \033[20;37mseen to \033[31m=>\033[92m {url} \033[31m|| \033[20;37mmethod \033[31m=> \033[92m{method} \033[31m||\033[20;37m time \033[31m=> \033[92m{date}\n')
try:
    file = open(proxi, 'r').read().split()
except:
    while True:
        print('\033[31m[!] \033[35mFile not Found')
        time.sleep(1)
        proxi:str = input('\n\033[35m[?] \033[36mproxy address _> \033[20;37m')
        try:
            file = open(proxi, 'r').read().split()
            break
        except:
            pass
file = open(proxi, 'r').read().split()
#.... ip creator ....
ip = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
#.........[start seener].........
for proxy in file:
    try:
        # 1 Method = telegram 
        if method == 1:
            # ....... cookie ..........
            try:
                r = requests.get('https://t.me/cd_home/3?embed=1', timeout=20, proxies={'http':'http://'+proxy})
                c = r.headers['set-cookie'].split(';')[0]
                # ......... key .......
                k = r.text.split('data-view="')[1].split('"')[0]
                if 'stel_ssid' in c:
                    c={'key':k,'cookie':c}
                else:
                    pass
            except Exception as e:
                pass
            try:
                r = requests.get(f'{url}?embed=1&view='+k, timeout=20, headers={'x-requested-with':'XMLHttpRequest','User-Agent': pyuseragents.random(),'referer':f'{url}?embed=1','cookie':c}, proxies={'http':'http://'+proxy})
                r.text
            except Exception as e:
                pass
            # headers 2
            headers={'x-requested-with':'XMLHttpRequest','user-agent': pyuseragents.random(),'referer':f'{url}?embed=1','cookie':c,'X-Forwarded-For': ip}
            requests.get(url, headers=headers, proxies={'http':'http://'+proxy},timeout=20)
            requests.get(url, proxies={'http':'http://'+proxy},timeout=20)
            print(f'\n\033[35m[+] \033[36mavailable \033[92m[proxy] \033[35m=> \033[93m{proxy}')
        # 2 Method = m.YouTube.com
        elif method == '2':
            head = {'user-agent': pyuseragents.random(),'Host':'https://m.YouTube.com','Content-Type': 'text/html; charset=utf-8', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Pragma': 'no-cache', 'Expires': 'Mon, 01 Jan 1990 00:00:00 GMT', 'Date': 'Fri, 15 Jul 2022 15:40:16 GMT', 'Strict-Transport-Security': 'max-age=31536000', 'X-Frame-Options': 'SAMEORIGIN', 'Cross-Origin-Opener-Policy-Report-Only': 'same-origin-allow-popups; report-to="youtube_main"', 'Permissions-Policy': 'ch-ua-arch=*, ch-ua-bitness=*, ch-ua-full-version=*, ch-ua-full-version-list=*, ch-ua-model=*, ch-ua-platform=*, ch-ua-platform-version=*', 'Report-To': '{"group":"youtube_main","max_age":2592000,"endpoints":[{"url":"https://csp.withgoogle.com/csp/report-to/youtube_main"}]}', 'P3P': 'CP="This is not a P3P policy! See http://support.google.com/accounts/answer/151657?hl=en for more info."', 'Content-Encoding': 'gzip', 'Server': 'ESF', 'X-XSS-Protection': '0', 'Set-Cookie': 'GPS=1; Domain=.youtube.com; Expires=Fri, 15-Jul-2022 16:10:16 GMT; Path=/; Secure; HttpOnly, YSC=XyyE4lQn8gY; Domain=.youtube.com; Path=/; Secure; HttpOnly; SameSite=none, VISITOR_INFO1_LIVE=gJto5usbMCY; Domain=.youtube.com; Expires=Wed, 11-Jan-2023 15:40:16 GMT; Path=/; Secure; HttpOnly; SameSite=none', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'Transfer-Encoding': 'chunked'}
            requests.get(url, headers=head, proxies={'http':'http://'+proxy},timeout=20)
            print(f'\n\033[35m[+] \033[36mavailable \033[92m[proxy] \033[35m=> \033[93m{proxy}')
        # 3 Method = YouTube.be
        elif method == 3:
            hed = {'Host':'https://youtu.be/','user-agent': pyuseragents.random(),'Content-Type': 'text/html; charset=utf-8', 'X-Content-Type-Options': 'nosniff', 'Cache-Control': 'no-cache, no-store, max-age=0, must-revalidate', 'Pragma': 'no-cache', 'Expires': 'Mon, 01 Jan 1990 00:00:00 GMT', 'Date': 'Fri, 15 Jul 2022 15:58:46 GMT', 'Strict-Transport-Security': 'max-age=31536000', 'X-Frame-Options': 'SAMEORIGIN', 'Cross-Origin-Opener-Policy-Report-Only': 'same-origin-allow-popups; report-to="youtube_main"', 'Permissions-Policy': 'ch-ua-arch=*, ch-ua-bitness=*, ch-ua-full-version=*, ch-ua-full-version-list=*, ch-ua-model=*, ch-ua-platform=*, ch-ua-platform-version=*', 'Report-To': '{"group":"youtube_main","max_age":2592000,"endpoints":[{"url":"https://csp.withgoogle.com/csp/report-to/youtube_main"}]}', 'P3P': 'CP="This is not a P3P policy! See http://support.google.com/accounts/answer/151657?hl=en for more info."', 'Content-Encoding': 'gzip', 'Server': 'ESF', 'X-XSS-Protection': '0', 'Set-Cookie': 'GPS=1; Domain=.youtube.com; Expires=Fri, 15-Jul-2022 16:28:46 GMT; Path=/; Secure; HttpOnly, YSC=tx0Hghd5J3U; Domain=.youtube.com; Path=/; Secure; HttpOnly; SameSite=none, VISITOR_INFO1_LIVE=5s9Vd6gboCo; Domain=.youtube.com; Expires=Wed, 11-Jan-2023 15:58:46 GMT; Path=/; Secure; HttpOnly; SameSite=none', 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'Transfer-Encoding': 'chunked'}
            requests.get(url, headers=hed, proxies={'http':'http://'+proxy})
            print(f'\n\033[35m[+] \033[36mavailable \033[92m[proxy] \033[35m=> \033[93m{proxy}')
        # 4 Method For Aparat
        elif method == 4:
            header = {'Host':'https://www.aparat.com/','user-agent': pyuseragents.random(),'server': 'nginx', 'date': 'Fri, 15 Jul 2022 16:50:19 GMT', 'content-type': 'text/html', 'content-length': '18289', 'last-modified': 'Mon, 11 Jul 2022 15:12:32 GMT', 'etag': '"62cc3de0-4771"', 'cache-control': 'no-cache', 'accept-ranges': 'bytes', 'x-frame-options': 'SAMEORIGIN', 'x-content-type-options': 'nosniff', 'x-xss-protection': '1; mode=block', 'referrer-policy': 'strict-origin-when-cross-origin','X-Forwarded-For': ip}
            requests.get(url, headers=header, proxies={'http':'http://'+proxy})
            print(f'\n\033[35m[+] \033[36mavailable \033[92m[proxy] \033[35m=> \033[93m{proxy}')
        # 5 Method For Pro All Url
        elif method == 5:
            req = requests.get(url,proxies={'http':'http://'+proxy})
            hd = {'Host': url, 'user-agent': pyuseragents.random(),'X-Forwarded-For': ip,'headers':req.headers}
            requests.get(url, headers=hd, proxies={'http':'http://'+proxy},timeout=20)
            print(f'\n\033[35m[+] \033[36mavailable \033[92m[proxy] \033[35m=> \033[93m{proxy}')
        # 6 Method Or 0 or Else For All Url
        else:
            requests.get(url, proxies={'http':'http://'+proxy},timeout=20)
            print(f'\n\033[35m[+] \033[36mavailable \033[92m[proxy] \033[35m=> \033[93m{proxy}')
    except:
        print(f'\n\033[31m[!] \033[35mFalse \033[35;37m[proxy] \033[31m=> \033[93m{proxy}')
#..............the...end................