__author__ = 'Pontsho Maseko'
__version__ = 1.0

import os
import json

from PySide2 import QtWidgets, QtGui, QtCore


class QtRootBrowser(QtWidgets.QWidget):

    _TYPES = ['File', 'Folder']
    gotFiles = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(QtRootBrowser, self).__init__(parent)

        # Layout
        m_layout = QtWidgets.QGridLayout()
        self.setLayout(m_layout)

        # Method label
        label = QtWidgets.QLabel('Qt Build Dir :                ')
        m_layout.addWidget(label, 0, 0)

        self._edit = QtWidgets.QLineEdit()
        m_layout.addWidget(self._edit, 0, 1)

        # Browse button
        browse_icon = QtGui.QIcon(':file-upload.png')
        browse_btn = QtWidgets.QPushButton()
        browse_btn.clicked.connect(self._browse)
        browse_btn.setFixedSize(35, 35)
        browse_btn.setIcon(browse_icon)
        browse_btn.setIconSize(QtCore.QSize(25, 25))
        m_layout.addWidget(browse_btn, 0, 2)

    def _browse(self):

        """Browse the file."""

        # Folder
        dialog = QtWidgets.QFileDialog()
        folder = dialog.getExistingDirectory()

        # Check for the rcc file
        found = False
        for item in os.listdir(folder):
            if item.startswith('rcc'):
                found = True
                break

        # Set text
        if found:

            # Settings path
            home = os.environ.get('HOME')
            settings_path = os.path.join(home, '.svg_to_qt', 'settings.json')

            # Get the settings
            with open(settings_path, 'r') as f:
                data = json.load(f)

            # Write the folder
            with open(settings_path, 'w') as f:
                data['qt_build_dir'] = folder
                json_data = json.dumps(data, indent = 4)
                f.write(json_data)

            # Set text
            self._edit.setText(folder)

        else:
            print('The folder given does not have the rcc executor')

    def set(self, path: str) -> None:
        self._edit.setText(path)

    def get(self) -> str:
        return self._edit.text()




