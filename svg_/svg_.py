__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['convert']


def convert(path, color, output=''):

	"""Changes the color of the svg and converts to png.
	:param path: The path to svg image.
	:param color: Hex code for the color to change to. 
	:param output: The output path of the new png.
	:return: Str
	"""

	# Check if the output path is given
	if output == '':
		output = path.replace('svg', 'png')