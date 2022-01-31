from PyQt5 import QtWidgets, QtGui, QtCore


class DNAGraphicsItem(QtWidgets.QGraphicsPolygonItem):
    """Class for a graphics item to use with DNA. Handles shape & colour.
        :parameter (string) dna type
        :inherits Qt.Widgets.QGraphicsPolygonItem"""
    def __init__(self, dna_type):
        super(DNAGraphicsItem, self).__init__()
        if dna_type == "a":
            self._construct_graphics_a()
        elif dna_type == "t":
            self._construct_graphics_t()
        elif dna_type == "c":
            self._construct_graphics_c()
        elif dna_type == "g":
            self._construct_graphics_g()

    def _construct_graphics_a(self):
        brushibrush = QtGui.QBrush(1)
        brushibrush.setColor(QtGui.QColor(255, 153, 153))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(9, 7))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 20))
        form.append(QtCore.QPointF(0, 20))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)

    def _construct_graphics_t(self):
        brushibrush = QtGui.QBrush(1)
        brushibrush.setColor(QtGui.QColor(204, 255, 153))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 7))
        form.append(QtCore.QPointF(9, 0))
        form.append(QtCore.QPointF(18, 7))
        form.append(QtCore.QPointF(18, 20))
        form.append(QtCore.QPointF(0, 20))
        form.append(QtCore.QPointF(0, 7))
        self.setPolygon(form)

    def _construct_graphics_c(self):
        brushibrush = QtGui.QBrush(1)
        brushibrush.setColor(QtGui.QColor(255, 204, 255))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(4.5, 7))
        form.append(QtCore.QPointF(9, 0))
        form.append(QtCore.QPointF(13.5, 7))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 20))
        form.append(QtCore.QPointF(0, 20))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)

    def _construct_graphics_g(self):
        brushibrush = QtGui.QBrush(1)
        brushibrush.setColor(QtGui.QColor(153, 153, 255))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 7))
        form.append(QtCore.QPointF(4.5, 0))
        form.append(QtCore.QPointF(9, 7))
        form.append(QtCore.QPointF(13.5, 0))
        form.append(QtCore.QPointF(18, 7))
        form.append(QtCore.QPointF(18, 20))
        form.append(QtCore.QPointF(0, 20))
        form.append(QtCore.QPointF(0, 7))
        self.setPolygon(form)

