__author__ = 'Pontsho Maseko'
__version__ = 1.0

import os

from svg_to_qt.core import maker, converter


def create():
    data = {
        'height' : 300,
        'width' : 300,
        'draws' : {
            'rect': {
                'x': 0,
                'y' : 0,
                'width': 200,
                'height': 200,
                'style': {
                    'fill': 'red'
                }
            }
        },
        'output': os.path.join(os.path.dirname(__file__), 'out.svg')
    }
    maker.create_svg(data)
    converter.convert(data['output'], 'red')