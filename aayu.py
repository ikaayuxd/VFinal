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
    def __init__(self, channel, post, http_sources=[], socks4_sources=[], socks5_sources=[], tasks=250):
        self.channel = channel
        self.post = post
        self.http_sources = http_sources
        self.socks4_sources = socks4_sources
        self.socks5_sources = socks5_sources
        self.tasks = tasks
        self.proxies = []
        self.success_sent = 0
        self.failed_sent = 0
        self.proxy_error = 0
        self.cookie_error = 0
        self.token_error = 0

    async def scrap(self, source_url, proxy_type):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(source_url, timeout=10) as response:
                    if response.status == 200:
                        proxies = REGEX.findall(await response.text())
                        for proxy in proxies:
                            self.proxies.append((proxy[0], proxy_type)) # Store proxy and type
                    else:
                        print(f"Error scraping proxies from {source_url}: Status code {response.status}")
        except Exception as e:
            print(f"Error scraping proxies from {source_url}: {e}")

    async def request(self, proxy, proxy_type):
        connector = aiohttp.TCPConnector(limit=0)
        if proxy_type != "http": # Use socks connector if not HTTP
            try:
                connector = aiohttp.ProxyConnector.from_url(f"{proxy_type}://{proxy[0]}")
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

    def run_proxies_tasks(self, lines: list, proxy_type):
        async def inner(proxies: list):
            await asyncio.gather( # Use gather for better exception handling
                *[asyncio.create_task(self.request(proxy, proxy_type)) for proxy in proxies]
            )

        chunks = [lines[i:i + self.tasks] for i in range(0, len(lines), self.tasks)]
        for chunk in chunks:
            asyncio.run(inner(chunk))

    async def init(self): # __init__ for initialization
        tasks = []
        self.proxies.clear() # Clear existing proxies before scraping new list of proxies
        for sources in (
                (self.http_sources, 'http'),
                (self.socks4_sources, 'socks4'),
                (self.socks5_sources, 'socks5')
        ):
            srcs, proxy_type = sources
            for source_url in srcs:
                task = asyncio.create_task(
                    self.scrap(source_url, proxy_type)
                )
                tasks.append(task)
        await asyncio.gather(*tasks) # gather for better exception handling
