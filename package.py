name = 'svg_to_qt'
version = '1.0.0'

build_command = 'python {root}/build.py'

tools = ['svg_to_qt']

requires = [
    'python-3.6+',
    'CairoSVG',
    'PySide2'
]

def commands():
    env.PATH.append('{root}/bin')
    env.PYTHONPATH.append('{root}/svg_to_qt')