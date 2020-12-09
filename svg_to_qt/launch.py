__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = 'standalone'

import sys
import os
import glob

# Add current dir to path
root = os.path.dirname(os.path.abspath(__file__))
paths = [
    root, os.path.join(root, 'core'), 
    os.path.join(root, 'resources'), 
    os.path.join(root, 'ui')
]
for path in paths:
    if not path in sys.path:
        sys.path.append(path)


from PySide2 import QtWidgets, QtGui

from ui import ui
from resources import resources


def standalone():

    """Launch standalone.
    :return: None.
    """


    # App and app style
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('fusion'))

    # Fonts dir
    fonts_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'resources/fonts')

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

    # Window
    win = ui.MakerUI()
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    standalone()