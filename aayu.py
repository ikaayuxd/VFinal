import requests
import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
import time

# Global variables
req_count = 0
lock = threading.Lock()

def read_proxies(proxy_type):
def read_proxies(proxy_type):
    proxies = []
    filename = f"{proxy_type}_proxies.txt"
    try:
        with open(filename, "r") as file:
            for line in file:
                proxy = line.strip()
                if proxy_type.startswith("socks") and ":" not in proxy: # Only add port to SOCKS if necessary
                    proxy += f":{port}"
                proxies.append(proxy)
    except FileNotFoundError:
        print(f"Error: {filename} file not found.")
        sys.exit(1)
    return proxies
    
def send_view(link, proxy):
    global req_count
    try:
        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'} if proxy else None

        session = requests.Session()
        if proxies:
            session.proxies.update(proxies)
        session.headers.update({
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        })

        main_res = session.get(link, timeout=10) # Add timeout
        main_res.raise_for_status()

        _token = main_res.text.split('data-view="')[1].split('"')[0]
        views_req = session.get("https://t.me/v/?views=" + _token, timeout=10) # Add timeout
        views_req.raise_for_status()


        with lock:
            req_count += 1
            print(f' [+] View Sent {req_count}/{count} Stats Code: {views_req.status_code} Proxy: {proxy if proxy else "None"}')
        time.sleep(random.uniform(1,3))

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e} Proxy: {proxy if proxy else 'None'}")
    except Exception as e:
        print(f"Error: {e} Proxy: {proxy if proxy else 'None'}")



if __name__ == "__main__":
    try:
        link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
        proxy_type = sys.argv[2].lower() # Get proxy type from command-line
        count = int(sys.argv[3])

        port = 33335 # Only used if you're using SOCKS proxies
        url_fin = f'https://{link}?embed=1'

        proxies = read_proxies(proxy_type) if proxy_type != "none" else [] # Handle "none" for no proxies


        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(send_view, url_fin, random.choice(proxies) if proxies else None) for _ in range(count)]


    except IndexError:
        print("""Error. Usage: python3 seen.py <link> <type> <count>
Types: http, socks4, socks5, mix, none""") # Added "none" option
    except ValueError:
        print("Error: Invalid count. Please enter an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
