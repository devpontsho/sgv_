__author__ = 'Pontsho Maseko'
__version__ = 1.0
__all__ = ['Primitive']

from PySide2 import QtWidgets, QtGui, QtCore


class Primitive():

    def __init__(self, name, _type):

        """Create primitive.
        :return: None.
        """
        self.shape = _type

    # -------------------------- Shape
    @property
    def shape(self):
        return self._shape

    @shape.setter
    def shape(self, _type):
        self._shape = _type

    # -------------------------- Name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # -------------------------- Color
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color
