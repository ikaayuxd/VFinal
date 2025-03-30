import requests
import random
import time
from itertools import cycle

url = 'https://t.me/LuxterCodes/9'

# Proxy list - FORMAT: ip:port or ip:port:user:pass
with open('../formatted_ips.txt', 'r') as file:
    proxies = [line.strip() for line in file.readlines()]
proxy_pool = cycle(proxies)


# User-Agent List (Spoof like a motherfucker)
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    # Add more user-agents, you lazy fuck
]


req_count = 0
retries = 3 # Retries per proxy

for i in range(len(proxies) * retries): # Iterate through proxies with retries
    try:
        proxy = next(proxy_pool)
        session = requests.session()
        session.proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }

        session.headers = {
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': random.choice(user_agents), # Randomize User-Agent
            'x-requested-with': 'XMLHttpRequest'
        }

        main_res = session.get(url)
        if main_res.status_code != 200:
            raise Exception(f"Shitty status code: {main_res.status_code}")


        _token = main_res.text.split('data-view="')[1].split('"')[0]


        views_req = session.get(f"https://t.me/v/?views={_token}")
        if views_req.status_code != 200:
            raise Exception(f"View request failed: {views_req.status_code}")

        print(f'[+] View Sent - Proxy: {proxy}, Status Code: {views_req.status_code}')
        req_count += 1
        time.sleep(random.uniform(1,3)) # Random delay to avoid detection, dumbass

    except Exception as e:
        print(f'Failed to send view using proxy {proxy}: {e}, Retrying...')
        # Don't fucking exit on error, retry with another proxy

print(f'Total views sent: {req_count}, You fucking legend!')
