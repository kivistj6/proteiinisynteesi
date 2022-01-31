from PyQt5 import QtWidgets, QtGui, QtCore


class IntronGraphicsItem(QtWidgets.QGraphicsPolygonItem):

    def __init__(self, dna_type, mutated):
        super(IntronGraphicsItem, self).__init__()
        self.mutated = mutated
        if dna_type == "a":
            self.construct_graphics_a()
        elif dna_type == "u":
            self.construct_graphics_u()
        elif dna_type == "c":
            self.construct_graphics_c()
        elif dna_type == "g":
            self.construct_graphics_g()

    def construct_graphics_a(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(204, 0, 0))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 20))
        form.append(QtCore.QPointF(9, 13))
        form.append(QtCore.QPointF(0, 20))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)

    def construct_graphics_u(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(204, 204, 0))
        self.setBrush(brushibrush)
        form = QtGui.QPolygonF()
        form.append(QtCore.QPointF(0, 0))
        form.append(QtCore.QPointF(18, 0))
        form.append(QtCore.QPointF(18, 13))
        form.append(QtCore.QPointF(9, 20))
        form.append(QtCore.QPointF(0, 13))
        form.append(QtCore.QPointF(0, 0))
        self.setPolygon(form)

    def construct_graphics_c(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(153, 0, 153))
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

    def construct_graphics_g(self):
        brushibrush = QtGui.QBrush(1)
        if self.mutated:
            brushibrush.setColor(QtGui.QColor(255, 0, 127))
        else:
            brushibrush.setColor(QtGui.QColor(102, 102, 255))
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
