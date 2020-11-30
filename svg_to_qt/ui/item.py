__author__ = 'Pontsho Maseko'
__version__ = 1.0

from PySide2 import QtWidgets, QtGui, QtCore
from ui import primitive

class Item(QtWidgets.QGraphicsItem):

    def __init__(self, name, rect):
        QtWidgets.QGraphicsItem.__init__(self)

        """Custum shape that will be turned into svg image.
        :param name: The name of the shape.
        :return: None.
        """

        self._bound_space = 6
        self.rect = rect
        self.radius = 0
        self._shapes = []

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def rect(self):
        return (self._rect, self._bounding)

    @rect.setter
    def rect(self, rect):

        """Bounding box.
        :type rect: QRectF.
        :return: None.
        """

        self._rect = rect
        self._bounding = QtCore.QRectF(
            rect.x() - (self._bound_space / 2), rect.y() - (self._bound_space / 2),
            rect.size().width() + self._bound_space, rect.size().height() + self._bound_space
        )

    def boundingRect(self):
        return self._bounding

    def addShape(self, shape):

        """Add another shape.
        :type shape: Primitive.
        :return: None.
        """

        self._shapes.append(shape)

    def paint(self, painter, option, widget):

        """Paint event the item.
        :type painter: QPainter
        :type option: QStyleOptionGraphicsItem
        :type widget: QWidget
        """

        print(self._shapes)
        
        painter.drawRoundedRect(self._rect, 5, 5)

    def mousePressEvent(self, event):

        """When the is pressed on the node.
        :param event: QMouseEvent
        :return: None.
        """

        if event.buttons() == QtCore.Qt.LeftButton:

            self._point = event.pos()
            event.accept()

        super()

        
