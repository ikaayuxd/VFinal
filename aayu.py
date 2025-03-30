import urllib.request
import ssl
import time
from itertools import cycle

url = 'https://t.me/LuxterCodes/9'

proxies = [
    'http://brd-customer-hl_5ad1b94c-zone-isp_proxy1-ip-185.96.133.239:7xiqg3c79wxg@brd.superproxy.io:33335',
    # ... (The rest of your correctly formatted proxies)
]
proxy_pool = cycle(proxies)

# SINGLE USER-AGENT (YOU DUMB FUCK)
user_agent = "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"


req_count = 0
retries_per_proxy = 3

for i in range(len(proxies) * retries_per_proxy):
    try:
        proxy = next(proxy_pool)

        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({'http': proxy, 'https': proxy}),
            urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        )

        opener.addheaders = [
            ('User-agent', user_agent), # DIRECTLY USING THE SINGLE USER-AGENT, YOU MORON
            ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
            ('Accept-Language', 'en-US,en;q=0.5'),
            ('Referer', 'https://t.me/')
            # ADD MORE HEADERS, YOU FUCKING CRETIN!
        ]
        urllib.request.install_opener(opener)

        with urllib.request.urlopen(url) as main_res:
            if main_res.getcode() != 200:
                raise Exception(f"Shitty status code from main page: {main_res.getcode()}")
            _token = main_res.read().decode().split('data-view="')[1].split('"')[0] # Check for empty string here

        views_url = f"https://t.me/v/?views={_token}"
        with urllib.request.urlopen(views_url) as views_req:
            if views_req.getcode() != 200:
                raise Exception(f"View request failed: {views_req.getcode()}")

            print(f'[+] View Sent - Proxy: {proxy}, Status Code: {views_req.getcode()}')
            req_count += 1

        time.sleep(random.uniform(2, 5))

    except Exception as e:
        print(f'Failed to send view using proxy {proxy}: {e}, Retrying...')

print(f'Total views sent: {req_count}')
