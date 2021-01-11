__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['generate_py_rcc', 'convert', 'generate_path', 'add_file_to_rcc']


import os
import random
import string
import cairosvg
import subprocess


def get_svgs(names, root, folders):
    
    """Get svgs from multiple folders.
    :param names: The names of the svg files.
    :param root: The root folder that the folders are in.
    :param folders: A list of folder names
    :return: List
    """
    
    svgs = []
    if len(folders) > 0 :
    
        for folder in folders:
            path = os.path.join(root, folder)
            contents = os.listdir(path)
            
            for item in contents:
                if item in names:
                    item_path = os.path.join(path, item)
                    svgs.append(item_path)
    
    else :
        
        contents = os.listdir(root)
        for item in contents:
            if item in names:
                item_path = os.path.join(root, item)
                svgs.append(item_path)
                
    return svgs


def generate_path(folder, exten='.svg', length=5):

	"""Generate a temporary path.
	:param folder: The path to the folder to save in.
	:param exten: The extern of the path that needs to be generated.
	:param length: The name length.
	:return: Str.
	"""

	name = ''
	for i in range(length):
		name += random.choice(string.ascii_letters)

	name += exten
	path = os.path.join(folder, name)
	return path


def generate_py_rcc(path, output=''):

	"""Generate python resource file for qt.
	:param path: the path the qrc file.
	:param output: The output path for python resource file.
	:return: 
	"""

	# Check if output path is provided.
	if output == '':
		output = path.replace('qrc', 'py')

	# Check if the output file exists
	if os.path.isfile(output):
		os.remove(output)

	# Convert
	command = 'pyside2-rcc {In} -o {Out}'.format(In=path, Out=output)
	pipe = subprocess.Popen(
		command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# Info
	for line in pipe.communicate(0):
		if line == b'':
			continue
		else:
			print(line)

	# Return
	print('Py Resource File : {}'.format(output))
	return output


def convert(path, color, _replace=True, output=''):

	"""Changes the color of the svg and converts to png.
	:param path: The path to svg image.
	:param color: Hex code for the color to change to.
	:param _replace: Should it replace files if they exist.
	:param output: The output path of the new png.
	:return: Str
	"""

	# Check if the output path is given
	if output == '':
		output = path.replace('.svg', '.png')

	# Delete output if exists
	if os.path.isfile(output) and _replace == True:
		os.remove(output)

	# Read the svg
	with open(path, 'r') as f:
		try:
			data = f.read()
		except:
			print('Failed to read : {}'.format(path))
			return

	# Fill in style
	if 'style' in data and 'fill:' in data:
		
		for code in data.split(' '):
			if code.startswith('style'):
				
				for style_tag in code.split('"'):
					if style_tag.startswith('fill'):
						new_style = code.replace(style_tag, 'fill:{};'.format(color))
						data = data.replace(code, new_style)

	# Fill without style
	elif 'fill=' in data:

		for code in data.split(' '):
			if code.startswith('fill'):
				data = data.replace(code, 'fill="{}"'.format(color))

	# Create 
	else:
		data = data.replace('path', 'path fill="{}"'.format(color))
	
	# Write out then new svg
	temp_out = generate_path(os.path.dirname(output))
	with open(temp_out, 'w') as f:
		f.write(data)
	
	# To PNG
	print('Temporary SVG : ', temp_out)
	cairosvg.svg2png(url=temp_out, write_to=output)
	print('Output : ', output)

	# Remove new svg
	try:
		os.remove(temp_out)
		print('Deleted : {}'.format(temp_out))
	except:
		print('Failed to delete : {}'.format(temp_out))


def generate_rcc(svgs, out_folder, color='#000000'):

	"""Will generate a rcc file for resources from svgs
	:param svgs: The list of svgs.
	:param out_folder: The output folder for the new png icons and resource file.
	:param color: The color to conver the svg file to, default is black.
	:return: Str.
	"""

	# qrc code
	qrc_code = '<!DOCTYPE RCC><RCC version="1.0">\n<qresource>'

	# Check if the out folder exists
	if not os.path.isdir(out_folder):
		os.mkdir(out_folder)

	# Get the icon folder
	icons_path = os.path.join(out_folder, 'icons')
	if not os.path.isdir(icons_path):
		os.mkdir(icons_path)

	# For every svg
	for svg in svgs:

		# PNG svg with the new color
		out = os.path.join(icons_path, os.path.basename(svg).replace('svg', 'png'))
		convert(svg, color, output=out)

		# Append to the qrc code
		qrc_code += '\n\t<file alias="{Alias}">{File}</file>'.format(Alias=os.path.basename(out), File=out)

	# Close the qrc code
	qrc_code += '\n</qresource>\n</RCC>'

	# Write out the qrc file
	qrc_file = os.path.join(out_folder, 'resources.qrc')
	with open(qrc_file, 'w') as f:
		f.write(qrc_code)

	# Return the resource file
	print('Resource File : {}'.format(qrc_file))

	# Generate resource
	py_rcc = generate_py_rcc(qrc_file)

	# Return
	return py_rcc


def add_file_to_rcc(resource_file, file):

	"""Add file to a resource file
	:param resource_file: The resource file.
	:param file: The file to add to the resource file.
	:return : None.
	"""

	# Get the qrc code
	with open(resource_file, 'r') as f:
		rc_code = f.read()

	# Lines of the rc code
	lines = rc_code.split('\n')

	# Code
	code = '\t<file alias="{Alias}">{File}</file>'.format(
		Alias=os.path.basename(file), File=file)

	# Add code to the lines
	lines.insert( len(lines) - 3, code)
	rc_code = '\n'.join(lines)

	# Write the rc code
	with open(resource_file, 'w+') as f:
		f.write(rc_code)

	# Generate the python resource file
	generate_py_rcc(resource_file)


