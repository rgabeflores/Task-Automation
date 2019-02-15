from urllib.parse import quote
from re import sub, MULTILINE
from os import mkdir, listdir
from os.path import isdir, exists
from shutil import copyfile

import sys
import logging

logging.basicConfig(level=logging.DEBUG)

'''
	USAGE:
		>> python script.py <MODE> <FILENAME>
	
	Encodes filenames for web server upload.
		-u UTF-8 Encoding
		-c Custom File Organization
	
	A folder with the files for input should be placed in /input/ folder.
	Resulting output files will be saved in the /output/ folder.
'''

try:
	MODE = sys.argv[1]
	FILES_DIR = quote(sys.argv[2])
except:
	print('USAGE:\n\t>> python script.py <MODE> <FILENAME>')
	sys.exit(1)

def utf8(files):
	return map(lambda x: quote(x), files)

def custom(files, files_dir):
	temp = (sub(' ','-',file, flags=MULTILINE) for file in files)
	return [f'{file[:-4]}_{files_dir}_{i}{file[-4:]}' for i, file in zip(range(len(files)),temp)]

def main(FILES_DIR):

	input_dir = f'./input/{FILES_DIR}'
	output_dir = f'./output/{FILES_DIR}'

	try:
		FILES = listdir(input_dir)
	except FileNotFoundError as e:
		logging.debug(e)
		sys.exit(1)

	if not(isdir(output_dir)):
		mkdir(output_dir)

	if MODE == '-u':
		results = utf8(FILES)
	elif MODE == '-c':
		results = custom(FILES, FILES_DIR)
	else:
		logging.debug('There is an issue with the MODE option.')
		sys.exit(1)

	[copyfile(
		f'{input_dir}/{FILE}', 
		f'{output_dir}/{result}'
		)
		for FILE, result in zip(FILES, results)
		]

	logging.info(f'Renamed files have been uploaded to ./output/{FILES_DIR}/')

if __name__ == '__main__':
	main(FILES_DIR)