__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['Canvas']

from PySide2 import QtWidgets, QtGui, QtCore

class Canvas(QtWidgets.QGraphicsView):

    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)

        # View
        self._scene = QtWidgets.QGraphicsScene(self)

