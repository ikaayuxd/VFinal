import requests
import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

# Global variables (generally try to minimize these)
req_count = 0
lock = threading.Lock() # For thread-safe incrementing of req_count

#=================================[PROXY]==========================================
def read_proxies(proxy_type): # Make proxy reading more flexible
    proxies = []
    filename = f"{proxy_type}_proxies.txt" # Construct filename based on type
    try:
        with open(filename, "r") as file:
            for line in file:
                proxy = line.strip()
                if proxy_type.startswith("socks"): # Add port for SOCKS proxies only if needed.
                    proxy += f":{port}"
                proxies.append(proxy)
    except FileNotFoundError:
        print(f"Error: {filename} file not found.")
    return proxies

#=================================[DEF]==========================================

def send_view(link, proxy, proxy_type):
    global req_count
    try:
        proxies = {
            'http': f'{proxy_type}://{proxy}',
            'https': f'{proxy_type}://{proxy}'
        } if proxy else None # Conditional proxies

        session = requests.Session()
        if proxies:
            session.proxies.update(proxies)
        session.headers.update({
            'accept-language': 'en-US,en;q=0.9',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest'
        })

        main_res = session.get(link)
        main_res.raise_for_status() # Check for bad status codes (4xx or 5xx)

        _token = main_res.text.split('data-view="')[1].split('"')[0]
        views_req = session.get("https://t.me/v/?views=" + _token)
        views_req.raise_for_status()

        with lock: # Thread-safe increment
            req_count += 1
            print(f' [+] View Sent {req_count}/{count} Stats Code: {views_req.status_code}')

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"Error: {e}")



#=================================[START]==========================================
if __name__ == "__main__":
    try:
        link = sys.argv[1].strip().replace('https://', '').replace('http://', '')
        proxy_type = sys.argv[2].lower()
        count = int(sys.argv[3])
        port = 33335 # Port - adjust if needed
        url_fin = f'https://{link}?embed=1'


        proxies = read_proxies(proxy_type)

        with ThreadPoolExecutor(max_workers=100) as executor: # Limiting number of workers
            futures = [executor.submit(send_view, url_fin, random.choice(proxies) if proxies else None, proxy_type) for _ in range(count)]


            # (Optional) You could process the results of the futures here if needed:
            # for future in concurrent.futures.as_completed(futures):
            #     try:
            #         future.result() # retrieve the result (or exception)
            #     except Exception as e:
            #         print(f"A thread failed: {e}")



    except IndexError:
        print("""Error. Usage: python3 seen.py <link> <type> <count>
Types: http, socks4, socks5, mix""")
    except ValueError:
        print("Error: Invalid count. Please enter an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
