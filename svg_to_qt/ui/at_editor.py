__author__ = 'Pontsho Maseko'
__version__ = 1.0

from PySide2 import QtWidgets, QtGui, QtCore

class AttributeEditor(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(AttributeEditor, self).__init__(parent)

        #
        self.setMinimumWidth(100)