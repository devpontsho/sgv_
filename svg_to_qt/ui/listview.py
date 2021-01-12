__author__ = 'Pontsho Maseko'
__version__ = 1.0

import os

from PySide2 import QtWidgets, QtGui, QtCore


class ListView(QtWidgets.QListView):

    def __init__(self, parent=None):
        super(ListView, self).__init__(parent)

        # Items
        self._paths = []

        # Set model
        model = QtGui.QStandardItemModel()
        self.setModel(model)

    def get_files(self):
        return self._paths

    def set_items(self, paths):

        model = self.model()
        for path in paths:

            if not path in self._paths:
                self._paths.append(path)

                item = QtGui.QStandardItem(path)
                model.appendRow(item)

    def clear(self):

        model = self.model()
        model.clear()
        self._paths = []
