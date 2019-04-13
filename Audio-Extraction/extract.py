from __future__ import unicode_literals
from os import chdir, mkdir, listdir, getcwd
from os.path import isfile
from contextlib import contextmanager

import youtube_dl
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

'''
	Extracts audio from url using youtube-dl. Takes one command line argument for the filename of the input. 
    The file should have a list of URLs delimited by new lines.
    Usage:
        >> python extract.py <filename>
'''

OUTPUT_PATH = './output/'

@contextmanager
def cd(dest):
    '''
        This function safely enters and exits a directory. 

        Usage:
            with cd("/path/to/directory"):
                # Code
    '''
    origin = getcwd()
    try:
        yield chdir(dest)
    finally:
        chdir(origin)


def extraction(urls):
    '''
        Retrieve the audio from the resources located at a given list of links
    '''
    YDL_OPTIONS = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    with cd(OUTPUT_PATH):
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            for url in urls:
                try:
                    ydl.download([url])
                except Exception as e:
                    logging.debug(e)


def main(FILE):

    if not(isfile(FILE)):
        print(f'Input file ({FILE}) does not exist')
        sys.exit(1)

    with open(f'./input/{FILE}', 'r') as f:
        urls = (line.strip() for line in f.readlines())
    extraction(urls)


if __name__ == '__main__':
    main(sys.argv[1])
