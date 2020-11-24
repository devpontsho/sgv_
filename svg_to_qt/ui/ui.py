__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['MakerUI']

from PySide2 import QtWidgets, QtGui, QtCore

from ui import canvas

class MakerUI(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MakerUI, self).__init__(parent)

        self.setWindowTitle('SVG Maker - 1.0')

        # Central widgey
        central = QtWidgets.QWidget()
        _layout = QtWidgets.QVBoxLayout()
        central.setLayout(_layout)

        scene = canvas.Canvas()
        _layout.addWidget(scene)
        
        self.setCentralWidget(central)

        # Attribute