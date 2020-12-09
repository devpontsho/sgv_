__author__ = 'Pontsho Maseko'
__version__ = 1.0

from PySide2 import QtWidgets, QtGui, QtCore


class Header(QtWidgets.QWidget):

    _title_text = ''

    def __init__(self, parent=None, title='', icon=':user-secrete.png' ):
        super(Header, self).__init__(parent)

        # Set parent
        self.main_window = None
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        self.setFixedHeight(20)

        # Icon size
        icon_size = QtCore.QSize(15, 15)

        # Main Layout
        m_layout = QtWidgets.QHBoxLayout()
        m_layout.setSpacing(0)
        m_layout.setMargin(0)
        self.setLayout(m_layout)

        size = self.size()
        self._spacer = QtWidgets.QSpacerItem(size.width() - 100, 0)

        # Title
        self._title = QtWidgets.QLabel()
        m_layout.addWidget(self._title)

        self.title = title

        # Spacer
        m_layout.addItem(self._spacer)


        # Buttons
        buttons_wid = QtWidgets.QWidget()
        buttons_wid.setFixedWidth(100)
        m_layout.addWidget(buttons_wid)

        # Buttons Layout
        button_lay = QtWidgets.QHBoxLayout()
        button_lay.setSpacing(0)
        button_lay.setMargin(0)
        buttons_wid.setLayout(button_lay)

        # Min Button
        min_icon = QtGui.QIcon(':window-minimize.png')
        min_btn = QtWidgets.QPushButton()
        min_btn.clicked.connect(self._minimize)
        min_btn.setIcon(min_icon)
        min_btn.setIconSize(icon_size)
        button_lay.addWidget(min_btn)

        # Max Button
        max_icon = QtGui.QIcon(':window-maximize.png')
        max_btn = QtWidgets.QPushButton()
        max_btn.clicked.connect(self._maximize)
        max_btn.setIcon(max_icon)
        max_btn.setIconSize(icon_size)
        button_lay.addWidget(max_btn)

        # Close Button
        close_icon = QtGui.QIcon(':window-close.png')
        close_btn = QtWidgets.QPushButton()
        close_btn.clicked.connect(self._close)
        close_btn.setIcon(close_icon)
        close_btn.setIconSize(icon_size)
        button_lay.addWidget(close_btn)


    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, text):
        
        self._title.setText(text)
        self._title_text = text

        size = self.size()
        print(self._title.size())

        self._spacer.changeSize(size.width() - 100, 0)

    @property
    def main_window(self):
        return self._parent

    @main_window.setter
    def main_window(self, widget):
        self._parent = widget

    def resizeEvent(self, event):
        
        e_size = event.size()
        self._spacer.changeSize(e_size.width() - 100, 0)

        super(Header, self).resizeEvent(event)

    def _close(self):

        if self._parent:
            self._parent.deleteLater()

            try:
                self._parent.accept()
            except:
                pass

    def _minimize(self):

        if self._parent:
            self._parent.setWindowState(QtCore.Qt.WindowMinimized)

    def _maximize(self):

        if self._parent:
            self._parent.setWindowState(QtCore.Qt.WindowMaximized)

        
