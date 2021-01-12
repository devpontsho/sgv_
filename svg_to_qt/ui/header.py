__author__ = 'Pontsho Maseko'
__version__ = 1.0

from PySide2 import QtWidgets, QtGui, QtCore


class Header(QtWidgets.QWidget):

    def __init__(self, parent=None, title=''):
        super(Header, self).__init__(parent)

        # Set
        self.setFixedHeight(30)

        # Main layout
        m_layout = QtWidgets.QHBoxLayout()
        m_layout.setMargin(2)
        self.setLayout(m_layout)

        # Button close
        close_icon = QtGui.QIcon(':window-close.png')
        close_btn = QtWidgets.QPushButton()
        close_btn.clicked.connect(self._close)
        close_btn.setFixedSize(25, 25)
        close_btn.setIcon(close_icon)
        close_btn.setIconSize(QtCore.QSize(20, 20))
        m_layout.addWidget(close_btn)

        # Minimize button
        min_icon = QtGui.QIcon(':window-minimize.png')
        min_btn = QtWidgets.QPushButton()
        min_btn.clicked.connect(self._minimize)
        min_btn.setFixedSize(25, 25)
        min_btn.setIcon(min_icon)
        min_btn.setIconSize(QtCore.QSize(20, 20))
        m_layout.addWidget(min_btn)

        # Left spacer
        left_spacer = QtWidgets.QSpacerItem(300, 0)
        m_layout.addItem(left_spacer)

        # Header
        label = QtWidgets.QLabel(title)
        m_layout.addWidget(label)

        # Right spacer
        right_spacer = QtWidgets.QSpacerItem(300, 0)
        m_layout.addItem(right_spacer)

    def _close(self):
        parent = self.parent()
        parent.deleteLater()

    def _minimize(self):
        parent = self.parent()
        parent.setAttribute(QtCore.Qt.WindowMinimized)