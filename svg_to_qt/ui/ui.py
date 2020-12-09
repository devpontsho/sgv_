__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['MakerUI']

from PySide2 import QtWidgets, QtGui, QtCore

from ui import canvas, at_editor, header

class MakerUI(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MakerUI, self).__init__(parent)

        # Set attributes
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setMinimumSize(700, 600)

        # Set Attributes
        self.radius = 0
        self.background = QtGui.QColor(62, 62, 62)
        self.foreground = QtGui.QColor(62, 62, 62)

        # Main Layout
        m_layout = QtWidgets.QVBoxLayout()
        self.setLayout(m_layout)


        # Header
        _header = header.Header(title='Maker - Untitled')
        _header.main_window = self
        m_layout.addWidget(_header)

        # Body
        body = QtWidgets.QSplitter()
        m_layout.addWidget(body)

        # Canvas
        self._canvas = canvas.Canvas()
        body.addWidget(self._canvas)

        # Attribute
        self._at = at_editor.AttributeEditor()
        body.addWidget(self._at)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, color):
        self._background = color

    @property
    def foreground(self):
        return self._foreground

    @foreground.setter
    def foreground(self, color):
        self._foreground = color

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    def _should_resize(self):

        rect = self.geometry()
        w, h = (rect.width(), rect.height())

        # Pos
        x, y = (rect.x(), rect.y())
        x_end, y_end = (x + w, y + h)

        g_x, g_y = (self._glob_pos.x(), self._glob_pos.y())
        #print(x_end, y_end, ' - ', g_x, g_y)



        return False

    def mouseMoveEvent(self, event):

        """Mouse is moveing
        :type event: QMouseMoveEvent
        :return: None.
        """

        if event.buttons() == QtCore.Qt.LeftButton:
            
            within = self._should_resize()


            drag_dist = QtWidgets.QApplication.startDragDistance()
            dist =  self._pos - event.pos()
            if dist.x() > drag_dist or dist.y() > drag_dist and within:

                if within:
                    print('Resizing')
                else:

                    self.move(self.pos() + (event.globalPos() - self._glob_pos))
                    self._glob_pos = event.globalPos()

        # Event
        super(MakerUI, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):

        """Mouse press
        :type event: QMousePressEvent
        :return: None.
        """

        # Left Mouse
        if event.buttons() == QtCore.Qt.LeftButton:
            self._pos = event.pos()
            self._glob_pos = event.globalPos()
        
        # Mouse press
        super(MakerUI, self).mousePressEvent(event)

    def paintEvent(self, event):

        """Paint event
        :return event: QPaintEvent()
        :return: None.
        """

        # Size of the widget
        size = self.size()

        # Paint
        painter = QtGui.QPainter()
        painter.begin(self)

        painter.setBrush(self._background)
        painter.setPen(self._foreground)
        painter.drawRoundRect(0, 0, size.width(), size.height(), self._radius, self._radius)

        painter.end()

        # Super
        super(MakerUI, self).paintEvent(event)