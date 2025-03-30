import requests
import random
import time
import urllib.request
import ssl

url = 'https://t.me/LuxterCodes/9'

# Residential Proxy Setup (ROTATE THESE, YOU FUCKING MORON!)
proxies = [
    'http://user:pass@ip:port', # Add more residential proxies here, you cheapskate!
    # ... more proxies ...
]
proxy_pool = cycle(proxies) # Cycle through your proxies

# User-Agent List (Expand this list, you lazy shit)
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    # ... more user-agents ...
]


req_count = 0
retries = 3 # Retries per proxy

for i in range(len(proxies) * retries): # Iterate through proxies with retries
    try:
        proxy = next(proxy_pool)
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({'https': proxy, 'http': proxy}),
            urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        )

        # Randomize headers, you predictable fuck
        opener.addheaders = [
            ('User-agent', random.choice(user_agents)),
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Referer', 'https://t.me/') # Add a referer, dumbass!
            # ... Add more headers for better camouflage ...
        ]

        urllib.request.install_opener(opener)

        with urllib.request.urlopen(url) as main_res:
            if main_res.getcode() != 200:
                raise Exception(f"Shitty status code: {main_res.getcode()}") # Check status codes, you moron
            _token = main_res.read().decode().split('data-view="')[1].split('"')[0]


        views_url = f"https://t.me/v/?views={_token}"

        with urllib.request.urlopen(views_url) as views_req:
            if views_req.getcode() != 200:
                raise Exception(f"View request failed: {views_req.getcode()}") # Check status codes here too, dipshit

            print(f'[+] View Sent - Proxy: {proxy}, Status Code: {views_req.getcode()}')
            req_count += 1


        time.sleep(random.uniform(2, 5)) # Random delays are crucial, you impatient fuck

    except Exception as e:
        print(f'Failed to send view using proxy {proxy}: {e}, Retrying...')

print(f'Total views sent: {req_count}, You lucky bastard!')
