__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = 'standalone'

import sys
import os
import glob

from PySide2 import QtWidgets, QtGui

from svg_to_qt.ui import ui
from svg_to_qt.resources import resources


def standalone():

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

    # Window
    win = ui.UI()
    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    standalone()