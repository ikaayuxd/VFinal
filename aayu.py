import urllib.request
import ssl
import random
import time

url = 'https://t.me/LuxterCodes/9'

# Residential Proxy (SINGLE - YOU'RE ASKING FOR TROUBLE, DUMBASS)
proxy = 'http://brd-customer-hl_5ad1b94c-zone-residential_proxy1:0lgchw232zru@brd.superproxy.io:33335'

# User-Agent List (STILL FUCKING ESSENTIAL, YOU MORON)
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    # ... ADD MORE, YOU LAZY SHIT ...
]

req_count = 0
retries = 3 # Retries (pointless with a single proxy, but whatever)


for i in range(retries): # Retrying with a single proxy is like fucking a dead horse
    try:
        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({'https': proxy, 'http': proxy}),
            urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        )

        # Headers for camouflage (STILL FUCKING IMPORTANT)
        opener.addheaders = [
            ('User-agent', random.choice(user_agents)),
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Referer', 'https://t.me/') # Referer for realism
            # ... MORE HEADERS, YOU FUCKING IDIOT ...
        ]

        urllib.request.install_opener(opener)


        with urllib.request.urlopen(url) as main_res:
            if main_res.getcode() != 200:
                raise Exception(f"Shitty status code: {main_res.getcode()}")
            _token = main_res.read().decode().split('data-view="')[1].split('"')[0]


        views_url = f"https://t.me/v/?views={_token}"
        with urllib.request.urlopen(views_url) as views_req:
            if views_req.getcode() != 200:
                raise Exception(f"View request failed: {views_req.getcode()}")

            print(f'[+] View Sent - Status Code: {views_req.getcode()}')
            req_count += 1


        time.sleep(random.uniform(2, 5)) # Delay (probably won't save you from getting blocked)

    except Exception as e:
        print(f'Failed to send view: {e}, Retrying... (This is pointless with a single proxy, you moron)')



print(f'Total views sent: {req_count} (Prepare for disappointment)')
