from __future__ import unicode_literals
from os import chdir, mkdir, listdir, path
from contextlib import contextmanager

import youtube_dl
import sys
import logging

logging.basicConfig(level=logging.DEBUG)
'''
	Extracts audio from url using youtube-dl
'''


@contextmanager
def dirwalk(x):
    if not(path.exists(x)):
        print('Output folder (./output/) does not exist')
        sys.exit(1)
    logging.info(f'Entering -> {x}')
    chdir(x)
    yield
    chdir('..')
    logging.info(f'Leaving -> {x}')


def extraction(urls):
    OUTPUT_PATH = './output/'

    with dirwalk(OUTPUT_PATH):
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            for url in urls:
                try:
                    ydl.download([url])
                except Exception as e:
                    logging.debug(e)


def main(FILE):

    if not(path.isfile(FILE)):
        print(f'Input file ({FILE}) does not exist')
        sys.exit(1)

    with open(f'./input/{FILE}', 'r') as f:
        urls = (line.strip() for line in f.readlines())
    extraction(urls)


if __name__ == '__main__':
    main(sys.argv[1])
