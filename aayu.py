import asyncio
import aiohttp
from re import compile, search

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36" # Rotating user-agents is highly recommended
REGEX = compile(
    r"(?:^|\D)?(("+ r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"):" + (r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
    + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])")
    + r")(?:\D|$)")


class ViewBot:
    def __init__(self, channel, post, proxy_file_path, tasks=250):
        self.channel = channel
        self.post = post
        self.proxy_file_path = proxy_file_path
        self.tasks = tasks
        self.proxies = []
        self.success_sent = 0
        self.failed_sent = 0
        self.proxy_error = 0
        self.cookie_error = 0
        self.token_error = 0

    async def request(self, proxy):
        connector = aiohttp.TCPConnector(limit=0)
        
        try:
            connector = aiohttp.ProxyConnector.from_url(f"http://{proxy}")
        except Exception as e:
            print(f"Error creating proxy connector: {e}")
            self.proxy_error += 1
            return # if proxy connector invalid - stop processing

        jar = aiohttp.CookieJar(unsafe=True)
        
        async with aiohttp.ClientSession(cookie_jar=jar, connector=connector) as session:
            try:
                async with session.get(
                        f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                        headers={
                            'referer': f'https://t.me/{self.channel}/{self.post}',
                            'user-agent': user_agent # Still single user-agent - VERY BAD. Needs rotation
                        },
                        timeout=aiohttp.ClientTimeout(total=5),
                        raise_for_status=True # raise error for bad status codes (4xx or 5xx)
                ) as embed_response:


                    views_token = search('data-view="([^"]+)"', await embed_response.text())
                    if views_token:
                        try:
                            views_response = await session.post(
                                'https://t.me/v/?views=' + views_token.group(1),
                                headers={
                                    'referer': f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                                    'user-agent': user_agent, # Again, needs rotation
                                    'x-requested-with': 'XMLHttpRequest'
                                },
                                timeout=aiohttp.ClientTimeout(total=5)
                            )
                            views_response.raise_for_status() # same here
                            if await views_response.text() == "true":
                                self.success_sent += 1
                            else:
                                self.failed_sent += 1 # Assuming server issues, bad proxy, rate limiting, etc.
                        except aiohttp.ClientError as e:
                            print(f"Error during views request: {e}")
                            self.failed_sent += 1 # HTTP errors
                        except Exception as e:
                           print(f"Other type of error during views request: {e}")
                           self.failed_sent += 1 # Any other errors



                    else:
                        self.token_error += 1
            except aiohttp.ClientError as e:
                print(f"Error during embed request: {e}")
                self.proxy_error +=1
            except Exception as e: # Catching general exceptions
                print(f"Other error during request: {e}")
                self.proxy_error += 1 # Count as proxy error (likely connection issue)
            finally:
                jar.clear()

    async def init(self): # __init__ for initialization
        tasks = []
        with open(self.proxy_file_path) as file:
            proxies = file.read().splitlines()
        
        self.proxies = proxies
        
        for chunk in range(0, len(proxies), self.tasks):
            tasks.append(asyncio.create_task(self.request_proxies(proxies[chunk:chunk+self.tasks])))
        
        await asyncio.gather(*tasks) # gather for better exception handling

    async def request_proxies(self, proxies):
        connector = aiohttp.TCPConnector(limit=0)
        
        async with aiohttp.ClientSession(connector=connector) as session:
            for proxy in proxies:
                try:
                    connector = aiohttp.ProxyConnector.from_url(f"http://{proxy}")
                    async with session.get(
                        f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                        headers={
                            'referer': f'https://t.me/{self.channel}/{self.post}',
                            'user-agent': user_agent # Still single user-agent - VERY BAD. Needs rotation
                        },
                        timeout=aiohttp.ClientTimeout(total=5),
                        raise_for_status=True # raise error for bad status codes (4xx or 5xx)
                    ) as embed_response:
                        views_token = search('data-view="([^"]+)"', await embed_response.text())
                        if views_token:
                            try:
                                views_response = await session.post(
                                    'https://t.me/v/?views=' + views_token.group(1),
                                    headers={
                                        'referer': f'https://t.me/{self.channel}/{self.post}?embed=1&mode=tme',
                                        'user-agent': user_agent, # Again, needs rotation
                                        'x-requested-with': 'XMLHttpRequest'
                                    },
                                    timeout=aiohttp.ClientTimeout(total=5)
                                )
                                views_response.raise_for_status() # same here
                                if await views_response.text() == "true":
                                    self.success_sent += 1
                                else:
                                    self.failed_sent += 1 # Assuming server issues, bad proxy, rate limiting, etc.
                            except aiohttp.ClientError as e:
                                print(f"Error during views request: {e}")
                                self.failed_sent += 1 # HTTP errors
                            except Exception as e:
                               print(f"Other type of error during views request: {e}")
                               self.failed_sent += 1 # Any other errors

                except aiohttp.ClientError as e:
                    print(f"Error during embed request: {e}")
                    self.proxy_error +=1
                except Exception as e: # Catching general exceptions
                    print(f"Other error during request: {e}")
                    self.proxy_error += 1 # Count as proxy error (likely connection issue)

async def main():
    channel = "LuxterCodes"
    post = "9"
    proxy_file_path = '../proxies.txt'
    tasks = 250

    bot = ViewBot(channel, post, proxy_file_path, tasks)
    await bot.init()

if __name__ == "__main__":
    asyncio.run(main())
