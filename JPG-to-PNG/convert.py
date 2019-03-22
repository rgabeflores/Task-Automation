from PIL import Image
from os import getcwd, listdir, chdir, makedirs, path
from contextlib import contextmanager
import sys

import logging

logging.basicConfig(level=logging.DEBUG)


BASE_PATH = getcwd()

logging.info(BASE_PATH)

@contextmanager
def enter_folder(folder):
	if not path.exists(folder):
		path_error(folder)
	chdir(folder)
	logging.info(f'Entering: {getcwd()}')
	yield
	logging.info(f'Leaving: {getcwd()}')
	if folder.startswith('..'):
		global BASE_PATH
		chdir(BASE_PATH)
	chdir('..')

def path_error(folder):
	print(f'No such folder exists: {folder}')
	print('NOTE: Original Images must be located in a folder named "jpg" or "png".\n')
	sys.exit(-1)

def png_to_jpg(folder):
	with enter_folder(f'./png/{folder}'):
		for file in listdir():
			if file[-4:] == '.png':
				try:
					img = Image.open(file)
				except Exception as e:
					logging.debug(e)
				else:
					if not path.exists(f'../jpg/{folder}'):
						makedirs(f'../jpg/{folder}')
					img = img.convert('RGB')
					img.save(f'../../jpg/{folder}/{file[0:-4]}.jpg')
					logging.info(f'Successful for {file}')

def jpg_to_png(folder):
	with enter_folder(f'./jpg/{folder}'):
		for file in listdir():
			if file[-4:] == '.jpg':
				try:
					img = Image.open(file)
				except Exception as e:
					logging.debug(e)
				else:
					if not path.exists(f'../../png/{folder}'):
						makedirs(f'../../png/{folder}')
					img.save(f'../../png/{folder}/{file[0:-4]}.png')
					logging.info(f'Successful for {file}')

def usage_error():
	print('Usage:\n\tpython convert.py <-pj,-jp> <filename> \n')
	sys.exit(-1)

def main():
	try:
		option = sys.argv[1]
			# int(input('''
			# (1) PNG to JPG
			# (2) JPG to PNG
			# '''
			# ))
		folder = sys.argv[2] #input('Enter the folder name containing the images:\n')
	except Exception as e:
		usage_error()

	if option == '-pj':
		png_to_jpg(folder)
	elif option == '-jp':
		jpg_to_png(folder)
	else:
		usage_error()

if __name__ == '__main__':
	main()