__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['generate_py_rcc', 'generate_binary_rcc', 'convert', 'generate_path', 'add_file_to_rcc']


import os
import random
import string
import cairosvg
import subprocess


def get_svgs(names: list, root: str, folders: list) -> list:
    
    """Get svgs from multiple folders.
    :param names: The names of the svg files.
    :param root: The root folder that the folders are in.
    :param folders: A list of folder names
    :return: list
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


def generate_rcc_output(qrc_file: str, rcc_type: str = 'python') -> list:

	"""Generate the output files for the compile resource files.
	:param qrc_file: The qrc file to compile
	:param rcc_type: The language to compile for.
	:return: list
	"""

	# Output files
	py_output = qrc_file.replace('qrc', 'py')
	binary_output = qrc_file.replace('qrc', 'rcc')

	# Command files
	py_command = f'pyside2-rcc {qrc_file} -o {py_output}'
	binary_command = f'rcc -binary {qrc_file} -o {binary_output}'

	# Check if the output file exists
	if rcc_type == 'python':
		if os.path.isfile(py_output):
			os.remove(py_output)

		return [py_output, py_command]

	else:
		if os.path.isfile(binary_output):
			os.remove(binary_output)

		return [binary_output, binary_command]


def generate_path(folder: str, exten: str = '.svg', length: int = 5) -> str:

	"""Generate a temporary path.
	:param folder: The path to the folder to save in.
	:param exten: The extern of the path that needs to be generated.
	:param length: The name length.
	:return: str.
	"""

	name = ''
	for i in range(length):
		name += random.choice(string.ascii_letters)

	name += exten
	path = os.path.join(folder, name)
	return path


def run_command(command: str) -> None:

	"""Generate python resource file for qt.
	:param path: Run the command.
	:return: None
	"""

	pipe = subprocess.Popen(
		command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	# Info
	for line in pipe.communicate(0):
		if line == b'':
			continue
		else:
			print(line)


def convert(path: str, color: str, _replace: bool = True, output: str = '') -> str:

	"""Changes the color of the svg and converts to png.
	:param path: The path to svg image.
	:param color: Hex code for the color to change to.
	:param _replace: Should it replace files if they exist.
	:param output: The output path of the new png.
	:return: str
	"""

	# Check if the output path is given
	if output == '':
		output = path.replace('.svg', '.png')
	else:
		output = output.replace('.svg', '.png')

	# Delete output if exists
	if os.path.isfile(output) and _replace == True:
		os.remove(output)

	# Read the svg
	with open(path, 'r') as f:
		try:
			data = f.read()
		except:
			print(f'Failed to read : {path}')
			return

	# Fill in style
	if 'style' in data and 'fill:' in data:
		
		for code in data.split(' '):
			if code.startswith('style'):
				
				for style_tag in code.split('"'):
					if style_tag.startswith('fill'):
						new_style = code.replace(style_tag, f'fill:{color};')
						data = data.replace(code, new_style)

	# Fill without style
	elif 'fill=' in data:

		for code in data.split(' '):
			if code.startswith('fill'):
				data = data.replace(code, f'fill="{color}"')

	# Create 
	else:
		data = data.replace('path', f'path fill="{color}"')
	
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
		print(f'Deleted : {temp_out}')
	except:
		print(f'Failed to delete : {temp_out}')


def generate_rcc(svgs: list, out_folder: str, color: str = '#000000', rcc_type: str = 'python') -> str:

	"""Will generate a rcc file for resources from svgs
	:param svgs: The list of svgs.
	:param out_folder: The output folder for the new png icons and resource file.
	:param color: The color to conver the svg file to, default is black.
	:param rcc_type: The language rcc to build for.
	:return: str.
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

	# Convert
	output, command = generate_rcc_output(qrc_file, rcc_type)
	run_command(command)

	# Status
	print(f'Resource File : {qrc_file}')
	print(f'Compile RCC File : {output}')

	# Return
	return output


def add_file_to_rcc(qrc_file: str, file: str, rcc_type: str = 'python') -> None:

	"""Add file to a resource file
	:param qrc_file: The resource file.
	:param file: The file to add to the resource file.
	:return : None.
	"""

	# Get the qrc code
	with open(qrc_file, 'r') as f:
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
	with open(qrc_file, 'w+') as f:
		f.write(rc_code)

	# Generate the resource file
	output, command = generate_rcc_output(qrc_file, rcc_type)
	run_command(command)

	# Status
	print(f'Resource File : {qrc_file}')
	print(f'Compile RCC File : {output}')


