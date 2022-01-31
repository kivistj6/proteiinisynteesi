from PyQt5 import QtWidgets, QtGui


class PeptideGraphicsItem(QtWidgets.QGraphicsEllipseItem):
    """Class for Peptide graphics item.
    :super is QtWidgets.QGraphicsEllipseItem
    Also has dictionary with peptide names and their colours."""

    peptideColors = {"Phe": QtGui.QColor(102, 0, 0), "Leu": QtGui.QColor(102, 51, 0), "Ile": QtGui.QColor(153, 153, 0),
                     "Met": QtGui.QColor(51, 102, 0), "Val": QtGui.QColor(0, 102, 0), "Ser": QtGui.QColor(0, 102, 51),
                     "Pro": QtGui.QColor(0, 102, 102), "Thr": QtGui.QColor(0, 51, 102), "Ala": QtGui.QColor(0, 0, 153),
                     "Tyr": QtGui.QColor(76, 0, 153), "His": QtGui.QColor(102, 0, 102), "Gln": QtGui.QColor(102, 0, 51),
                     "Asn": QtGui.QColor(153, 0, 0), "Lys": QtGui.QColor(153, 76, 0), "Asp": QtGui.QColor(76, 153, 0),
                     "Glu": QtGui.QColor(0, 153, 153), "Cys": QtGui.QColor(0, 76, 153), "Trp": QtGui.QColor(153, 0, 153),
                     "Arg": QtGui.QColor(153, 0, 76), "Gly": QtGui.QColor(204, 0, 102), "Ochre": QtGui.QColor(255, 128, 0),
                     "Amber": QtGui.QColor(255, 195, 51), "Opal": QtGui.QColor(222, 224, 224)}

    def __init__(self):
        super(PeptideGraphicsItem, self).__init__()
        self.setRect(0, 0, 58, 58)
