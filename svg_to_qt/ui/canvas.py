__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['Canvas']


from PySide2 import QtWidgets, QtGui, QtCore
from ui import item


class Canvas(QtWidgets.QGraphicsView):

    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)

        # Transform
        self._transform = QtGui.QTransform()

        # Scene
        rect = QtCore.QRectF(0, 0, 700, 500)
        self._scene = QtWidgets.QGraphicsScene(rect)
        self.setScene(self._scene)

        # Rectangle
        rectangle = QtCore.QRectF(30, 30, 100, 50)

        _item = item.Item('Hello', rectangle)
        
        self._scene.addItem(_item)

    def resizeEvent(self, event):

        """Resizing.
        :param event: QResizeEvent()
        :return: None.
        """

        size = event.size()
        self._scene.update(0, 0, size.width(), size.height())

        super(Canvas, self).resizeEvent(event)

    def mousePressEvent(self, event):

        """Mouse Press.
        :param event: QMousePressEvent()
        :return: None.
        """
        
        cursor_point = event.pos()
        print(self._scene.itemAt(cursor_point, self._transform))

        super(Canvas, self).mousePressEvent(event)


        

