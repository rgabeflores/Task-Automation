from os import mkdir, listdir
from os.path import isdir, exists
from PIL import Image
from shutil import copyfile

import sys
import logging

logging.basicConfig(level=logging.DEBUG)

'''
	USAGE:
		>> python thumbs.py <FOLDER NAME>
	
	
	Creates thumbnails with specified ratio
'''

DIMENSIONS = (560, 420) # 4:3 Aspect Ratio

try:
	FILES_DIR = sys.argv[1]
except:
	print('USAGE:\n\t>> python thumbs.py <FOLDER NAME>')
	sys.exit(1)

def validate(width, height, ratio, grow=False):
	'''
		Validates and/or recalculates width and height based on target aspect ratio or proportion.
		width - initial width
		height - initial height
		ratio - target aspect ratio/proportion
		grow - increase or decrease area
	'''

	r = width / height

	if grow:
		if r < ratio: # Alter Height
			width = height * ratio
		if r > ratio: # Alter Width
			height = width * (1 / ratio)
	else:
		if r < ratio: # Alter Height
			height = width * (1 / ratio)
		if r > ratio: # Alter Width
			width = height * ratio
		
	return (width, height)

def build(file, size):
	img = Image.open(file)
	img.thumbnail(size)

	width, height = img.size

	logging.debug(f'FILE: {file}')

	width, height = validate(width, height, size[0] / size[1])
	
	img = img.crop((0,0,width,height))
	img.save(file)

def main(FILES_DIR, DIMENSIONS):
	INPUT_PATH = f'./input/{FILES_DIR}'
	OUTPUT_PATH = f'./output/{FILES_DIR}'

	try:
		FILES = listdir(INPUT_PATH)
	except FileNotFoundError as e:
		logging.debug(e)
		sys.exit(1)

	if not(isdir(OUTPUT_PATH)):
		mkdir(OUTPUT_PATH)

	FILES = list(filter(lambda x: x[-4:] == '.jpg' or x[-4:] == '.png', FILES))

	SRC_FILES = [f'{INPUT_PATH}/{FILE}' for FILE in FILES]
	DST_FILES = [f'{OUTPUT_PATH}/{FILE}' for FILE in FILES]

	[copyfile(
		src,
		dst
		)
		for src, dst in zip(SRC_FILES, DST_FILES)
		]

	[build(dst, DIMENSIONS) for dst in DST_FILES]

	logging.info(f'Thumbnails were saved in {OUTPUT_PATH}')

if __name__ == '__main__':
	main(FILES_DIR, DIMENSIONS)