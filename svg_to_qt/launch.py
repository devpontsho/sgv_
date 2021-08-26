__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = 'standalone'

import sys
import json
import os
import glob

from PySide2 import QtWidgets, QtGui

from svg_to_qt.ui import ui
from svg_to_qt.resources import resources


def get_qt_build_dir() -> str:

    """Gets the qt build directory.
    return: str"""

    home = os.environ.get('HOME')
    settings_path = os.path.join(home, '.svg_to_qt', 'settings.json')
    settings_dir = os.path.dirname(settings_path)

    # Check if the directory exists
    if not os.path.isdir(settings_dir):
        os.mkdir(settings_dir)

    # Create the file if does not exist
    if not os.path.isfile(settings_path):
        with open(settings_path, 'w') as f:
            data = json.dumps({'qt_build_dir' : ''}, indent=4)
            f.write(data)

        return ''

    with open(settings_path, 'r') as f:
        data = json.load(f)
        return data.get('qt_build_dir')


def standalone() -> None:

    """Launch standalone.
    :return: None.
    """

    # Environment for Mac's new OS
    os.environ['QT_MAC_WANTS_LAYER'] = '1'

    # Root folder
    root = os.path.dirname(os.path.abspath(__file__))

    # App and app style
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('fusion'))

    # Fonts dir
    fonts_dir = os.path.join(
        os.path.dirname(root), 'resources/fonts')

    # Get fonts
    fonts = glob.glob('{}/*/*.ttf'.format(fonts_dir), recursive=True)

    # Add fonts
    for font in fonts:
        QtGui.QFontDatabase.addApplicationFont(font)

    # Read the stylesheet
    with open('{}/resources/style.qss'.format(root), 'r') as f:
        stylesheet = f.read()

    # Set stylesheet
    app.setStyleSheet(stylesheet)

    # Get Qt build dir
    qt_build_dir = get_qt_build_dir()

    # Window
    win = ui.UI()
    win.set_qt_build_dir(qt_build_dir)
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    standalone()