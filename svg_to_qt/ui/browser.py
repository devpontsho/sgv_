__author__ = 'Pontsho Maseko'
__version__ = 1.0

import os

from PySide2 import QtWidgets, QtGui, QtCore


class Browser(QtWidgets.QWidget):

    _TYPES = ['File', 'Folder']
    gotFiles = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(Browser, self).__init__(parent)

        # Layout
        m_layout = QtWidgets.QGridLayout()
        self.setLayout(m_layout)

        # Method label
        method_label = QtWidgets.QLabel('Type :                ')
        m_layout.addWidget(method_label, 0, 0)

        # Method
        self._method_box = QtWidgets.QComboBox()
        for t in self._TYPES:
            self._method_box.addItem(t)
        m_layout.addWidget(self._method_box, 0, 1)

        # Label
        edit_label = QtWidgets.QLabel('Browser : ')
        m_layout.addWidget(edit_label, 1, 0)

        # Text edit
        self._edit = QtWidgets.QLineEdit()
        m_layout.addWidget(self._edit, 1, 1)

        # Browse button
        browse_icon = QtGui.QIcon(':file-upload.png')
        browse_btn = QtWidgets.QPushButton()
        browse_btn.clicked.connect(self._browse)
        browse_btn.setFixedSize(35, 35)
        browse_btn.setIcon(browse_icon)
        browse_btn.setIconSize(QtCore.QSize(25, 25))
        m_layout.addWidget(browse_btn, 1, 2)

    def _browse(self) -> None:

        """Browse the file."""

        # Method
        text = ''
        value = ''
        method = self._TYPES[self._method_box.currentIndex()]

        # Get file(s) or folder
        dialog = QtWidgets.QFileDialog()
        if method == 'Folder':

            # Folder
            folder = dialog.getExistingDirectory()
            value = []

            # Get SVG(s) in the folder
            for item in os.listdir(folder):
                if item.endswith('.svg'):
                    path = os.path.join(folder, item)
                    if not path in value:
                        value.append(path)
        else:
            value = dialog.getOpenFileNames()[0]

        # Check if we got a list
        if isinstance(value, list):
            value = ';'.join(value)

        # Edit
        self._edit.setText(value)
        self.gotFiles.emit(value.split(';'))

    def get(self) -> list:
        return self._edit.text().split(';')




