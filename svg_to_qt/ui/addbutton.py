__author__ = 'Pontsho Maseko'
__version__ = 1.0

from PySide2 import QtWidgets, QtGui, QtCore


class AddButton(QtWidgets.QPushButton):

    gotFiles = QtCore.Signal(list)

    def __init__(self, parent=None):
        super(AddButton, self).__init__(parent)

        # Set
        self.setMinimumSize(300, 100)
        self.setAcceptDrops(True)

        # Icon
        icon = QtGui.QIcon(':plus-square.png')
        self.setIcon(icon)
        self.setIconSize(QtCore.QSize(100, 100))

        # Click
        self.clicked.connect(self._browser)

    def _browser(self):

        # File dialog
        dialog = QtWidgets.QFileDialog()
        files = dialog.getOpenFileNames()[0]

        # Check if files were selected
        if len(files) > 0:
            self.gotFiles.emit(files)

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):

        # Data
        mimedata = event.mimeData()

        # check for urls
        if mimedata.hasUrls():

            # Get the files
            files = []
            for url in mimedata.urls():
                files.append(url.path())

            # Emit the signal with files
            if len(files) > 0:
                self.gotFiles.emit(files)

        # Accept event
        event.acceptProposedAction()