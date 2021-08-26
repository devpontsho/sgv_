name = 'svg_to_qt'
version = '1.0.0'

build_command = False

requires = [
    'python-3.6+',
    'CairoSVG',
    'PySide2'
]

def commands():
    env.PYTHONPATH.append('{root}/svg_to_qt')