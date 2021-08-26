__author__ = 'Pontsho Maseko'
__version__ = 1.0

from PySide2 import QtWidgets, QtGui, QtCore


class Color(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Color, self).__init__(parent)

        # Main
        m_layout = QtWidgets.QGridLayout()
        self.setLayout(m_layout)

        # label
        label = QtWidgets.QLabel('Color :               ')
        m_layout.addWidget(label, 0, 0)

        # Edit
        self._edit = QtWidgets.QLineEdit()
        m_layout.addWidget(self._edit, 0, 1)

        # Button
        icon = QtGui.QIcon(':eye-dropper.png')
        btn = QtWidgets.QPushButton()
        btn.clicked.connect(self._pick)
        btn.setFixedSize(35, 35)
        btn.setIcon(icon)
        btn.setIconSize(QtCore.QSize(25, 25))
        m_layout.addWidget(btn, 0, 2)

    def _pick(self) -> None:

        # Color picker
        dialog = QtWidgets.QColorDialog()
        c = dialog.getColor()

        # Hex color
        hex_color = c.name()
        self._edit.setText(hex_color)

    def get(self) -> str:
        return self._edit.text()
