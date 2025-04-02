import requests
import random
import sys
import threading

#=================================[PROXY]==========================================
def read_proxies():
    proxies = []
    try:
        with open("http_proxies.txt", "r") as file:
            for line in file:
                proxy = line.strip() + ":" + str(port)
                proxies.append(proxy)
    except FileNotFoundError:
        print("Error: http_proxies.txt file not found.")
    return proxies

#=================================[DEF]==========================================

def socks4_start(link):
    global proxy_4, count, req_count
    while req_count < int(count):
        proxy = random.choice(proxy_4)
        try:
            session = requests.session()
            session.proxies.update({'http': f'socks4://{proxy}', 'https': f'socks4://{proxy}'})
            session.headers.update({
                'accept-language': 'en-US,en;q=0.9',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'
                })
            main_res = session.get(link)
            _token = main_res.text.split('data-view="')[1].split('"')[0]
            views_req = session.get("https://t.me/v/?views=" + _token)
            print(' [+] View Sent ' + 'Stats Code: '+str(views_req.status_code))
            req_count += 1
        except:
            pass

# Modify the other functions (socks5_start and http_start) in a similar way.

#=================================[START]==========================================
try:
    count = sys.argv[3]
    req_count = 0
    link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
    url_fin = f'https://{link}?embed=1'
    
    port = 33335
    
    if sys.argv[2] == "socks4":
        proxy_4 = read_proxies()
        for _ in range(int(count)):
            threading.Thread(target=socks4_start,args=(url_fin,)).start()

    # Modify the other conditions (socks5, http, mix) in a similar way.
    
except Exception as e:
    print(e)
    print("""Error . Help : python3 seen.py <link> <type> <count>
Types : http , socks4 , socks5 , mix
""")
