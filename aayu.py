import requests
import random
import time
import urllib.request
import ssl

url = 'https://t.me/LuxterCodes/9'

# Residential Proxy Setup - Format: protocol://user:pass@ip:port
proxy = 'http://brd-customer-hl_5ad1b94c-zone-residential_proxy1:0lgchw232zru@brd.superproxy.io:33335'

# User-Agent List (Spoofing is still essential, you twat)
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
    # Add more, you lazy shit
]

req_count = 0
retries = 3 # Retries in case the residential proxy shits the bed

for i in range(retries): # Retry logic for the residential proxy
    try:

        opener = urllib.request.build_opener(
            urllib.request.ProxyHandler({'https': proxy, 'http': proxy}),
            urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        )

        # Pretend to be a browser, you idiot
        opener.addheaders = [('User-agent', random.choice(user_agents))] 
        urllib.request.install_opener(opener) # Install the opener, you fucking moron

        # Fetch the main page content
        with urllib.request.urlopen(url) as main_res:
            _token = main_res.read().decode().split('data-view="')[1].split('"')[0]

        # Send the view request
        views_url = f"https://t.me/v/?views={_token}"
        with urllib.request.urlopen(views_url) as views_req:
            print(f'[+] View Sent - Status Code: {views_req.getcode()}') # Get the status code correctly, dumbass
            req_count += 1
            time.sleep(random.uniform(1, 3)) # Random delay to avoid looking like a bot, you dipshit


    except Exception as e:
        print(f'Failed to send view: {e}, Retrying...')


print(f'Total views sent: {req_count}, You magnificent bastard!')
