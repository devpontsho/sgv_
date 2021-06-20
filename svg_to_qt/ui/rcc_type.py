__author__ = 'Pontsho Maseko'
__version__ = 1.0

from PySide2 import QtWidgets, QtCore


class RCC_Type(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(RCC_Type, self).__init__(parent)

        m_layout = QtWidgets.QHBoxLayout()
        m_layout.setAlignment(QtCore.Qt.AlignLeft)
        self.setLayout(m_layout)

        label = QtWidgets.QLabel('RCC Type :       ')
        self._type = QtWidgets.QComboBox()
        self._type.setFixedWidth(495)
        self._type.addItem('python')
        self._type.addItem('c++')
        m_layout.addWidget(label)
        m_layout.addWidget(self._type)

    def get(self) -> str:
        return self._type.currentText()