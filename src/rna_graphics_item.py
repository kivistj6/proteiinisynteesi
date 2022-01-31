from PyQt5 import QtWidgets, QtGui, QtCore


class RNAGraphicsItem(QtWidgets.QGraphicsPolygonItem):
    """Class for a graphics item to use with RNA. Handles shape & colour.
    :param (string) dna type and (boolean) telling if there is a mutation.
    :super Qt.Widgets.QGraphicsPolygonItem"""
    def __init__(self, dna_type, mutated):
        super(RNAGraphicsItem, self).__init__()
        self.mutated = mutated
        if dna_type == "a":
            self._construct_graphics_a()
        elif dna_type == "u":
            self._construct_graphics_u()
        elif dna_type == "c":
            self._construct_graphics_c()
        elif dna_type == "g":
            self._construct_graphics_g()

    def _construct_graphics_a(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(255, 153, 153))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 20))
        form.append(QtCore.QPointF(9, 13))
        form.append(QtCore.QPointF(0, 20))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)

    def _construct_graphics_u(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(255, 255, 153))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 13))
        form.append(QtCore.QPointF(9, 20))
        form.append(QtCore.QPointF(0, 13))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)

    def _construct_graphics_c(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(255, 204, 255))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 20))
        form.append(QtCore.QPointF(13.5, 13))
        form.append(QtCore.QPointF(9, 20))
        form.append(QtCore.QPointF(4.5, 13))
        form.append(QtCore.QPointF(0, 20))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)

    def _construct_graphics_g(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(153, 153, 255))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 13))
        form.append(QtCore.QPointF(13.5, 20))
        form.append(QtCore.QPointF(9, 13))
        form.append(QtCore.QPointF(4.5, 20))
        form.append(QtCore.QPointF(0, 13))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)
