from urllib.request import urlopen, urlretrieve
from urllib.parse import urlparse, urlunparse
from bs4 import BeautifulSoup
import asyncio
import concurrent.futures

import sys
import logging

logging.basicConfig(level=logging.DEBUG)

info = '''
    USAGE:
        >> python scrape.py <url>
'''


def get_paths(url):
    response = urlopen(url)
    content = response.read()
    page = BeautifulSoup(content, 'html.parser')

    imgs = page.findAll('img')
    imgs = list(filter(lambda x: not(x['src'] is None), imgs))

    srcs = [img['src'] for img in imgs]

    return srcs


def sanitize(url):
    logging.info(url)
    parsed_url = urlparse(url)
    if parsed_url.netloc is '':
        return 'https://youtube.com{}'.format(url)
    return url


async def main():
    img_paths = get_paths(sys.argv[1])
    logging.info(f'Number of Links Found: {len(img_paths)}')
    img_paths = list(map(sanitize, img_paths))

    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor,
                urlretrieve,
                img_path,
                f'./results/{i}.jpg'

            )
            for i, img_path in zip(range(len(img_paths)), img_paths)
        ]

        for result in await asyncio.gather(*futures):
            pass

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
