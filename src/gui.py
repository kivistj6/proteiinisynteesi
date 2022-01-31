from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit, QGraphicsScene, QGraphicsView
from PyQt5 import QtGui, QtWidgets

from protein_synthesis import ProteinSynthesis
from rna_graphics_item import RNAGraphicsItem
from dna_graphics_item import DNAGraphicsItem
from peptide_graphics_item import PeptideGraphicsItem
from intron_graphics_item import IntronGraphicsItem
from exception import InvalidDNASequence, EmptyRnaException


class UI(QGraphicsView):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Protein Synthesis Simulation")
        self.synthesis = None
        self.scene = QGraphicsScene()
        self.show_choose_file("Give File Name:")

    def show_choose_file(self, message: str):
        self.scene = QGraphicsScene()
        self.setGeometry(100, 100, 420, 210)
        message_label = QLabel()
        message_label.setText(message)
        message_label.move(80, 10)
        self.scene.addWidget(message_label)
        self.name_field = QLineEdit()
        self.name_field.move(80, 30)
        self.scene.addWidget(self.name_field)

        error_label = QLabel()
        error_label.setText("Give Error Rate (e.g. 0.001):")
        error_label.move(80, 60)
        self.scene.addWidget(error_label)
        self.error_field = QLineEdit()
        self.error_field.move(80, 80)
        self.scene.addWidget(self.error_field)

        load_button = QPushButton("Run")
        load_button.move(80, 120)
        load_button.clicked.connect(self.handle_load_file)
        self.scene.addWidget(load_button)
        self.setScene(self.scene)
        self.show()

    def handle_load_file(self):

        self.synthesis = ProteinSynthesis(self.name_field.text(), self.error_field.text())
        try:
            self.synthesis.run_protein_synthesis()

        except OSError:
            self.show_choose_file("File error or file not found. Choose another file.")
        except InvalidDNASequence as e:
            self.show_choose_file(e.__str__()+" - Choose another file.")
        except EmptyRnaException as e:
            self.show_choose_file(e.__str__()+" - Choose another file.")
        except Exception as e:
            self.show_choose_file(e.__str__() + " - Choose another file.")
        else:
            self.show_protein_synthesis()

    def show_protein_synthesis(self):
        self.scene = QGraphicsScene()
        self.setGeometry(100, 100, 1280, 720)
        rna = self.synthesis.rna.getRNA()
        pre = self.synthesis.rna.getPremRNA()
        dna = self.synthesis.dna.getDNA()

        nucleus = QtWidgets.QGraphicsRectItem(0, 0, len(dna)*20+20, 190)
        self.scene.addItem(nucleus)
        title_n = QLabel()
        title_n.setAutoFillBackground(True)
        title_n.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 15pt;")
        title_n.setText("NUCLEUS")
        title_n.move(15, 10)
        self.scene.addWidget(title_n)
        brush = QtGui.QBrush(1)
        brush.setColor(QtGui.QColor(153, 76, 0, 110))
        nucleus.setBrush(brush)

        ribosome = QtWidgets.QGraphicsRectItem(0, 210, len(rna)*20+20, 190)
        self.scene.addItem(ribosome)
        title_r = QLabel()
        title_r.setAutoFillBackground(True)
        title_r.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 15pt;")
        title_r.setText("RIBOSOME")
        title_r.move(15, 220)
        self.scene.addWidget(title_r)
        brush.setColor(QtGui.QColor(102, 102, 0, 100))
        ribosome.setBrush(brush)

        title_d = QLabel()
        title_d.setAutoFillBackground(True)
        title_d.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 12pt;")
        title_d.setText("DNA")
        title_d.move(15, 123)
        self.scene.addWidget(title_d)

        title = QLabel()
        title.setAutoFillBackground(True)
        title.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 12pt;")
        title.setText("RNA")
        title.move(self.synthesis.dna.rna_start*20+10, 57)
        self.scene.addWidget(title)

        title2 = QLabel()
        title2.setAutoFillBackground(True)
        title2.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 11pt;")
        title2.setText("RNA")
        title2.move(15, 257)
        self.scene.addWidget(title2)

        title3 = QLabel()
        title3.setAutoFillBackground(True)
        title3.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 11pt;")
        title3.setText("Peptide Chain")
        title3.move(15, 367)
        self.scene.addWidget(title3)

        mut = QLabel()
        mut.setAutoFillBackground(True)
        mut.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 11pt; color: rgb(255, 0, 127); font-weight: 700")
        mut.setText("Mutations")
        mut.move(15, 35)
        self.scene.addWidget(mut)

        intronStart = self.synthesis.dna.rna_start + self.synthesis.rna.intron_start
        intronEnd = self.synthesis.dna.rna_start + self.synthesis.rna.intron_end
        if self.synthesis.rna.intron_start == 0:
            intronStart = self.synthesis.dna.rna_start + len(rna)
            intronEnd = intronStart + 1

        for i in range(len(dna)):
            if i >= self.synthesis.dna.rna_start and i-self.synthesis.dna.rna_start < len(pre):
                mutated = False
                if i-self.synthesis.dna.rna_start in self.synthesis.rna.faulty_reads:
                    mutated = True
                if intronEnd > intronStart:
                    if intronStart <= i < intronEnd:
                        item = IntronGraphicsItem(pre[i - self.synthesis.dna.rna_start], mutated)
                        item.moveBy(i * 20 + 10, 80)
                        self.scene.addItem(item)
                        letter = QLabel()
                        letter.setAutoFillBackground(True)
                        letter.setStyleSheet("background-color: rgba(1, 0, 0, 0)")
                        letter.setText(pre[i - self.synthesis.dna.rna_start].upper())
                        letter.move(i * 20 + 16, 80)
                        self.scene.addWidget(letter)
                    else:
                        item = RNAGraphicsItem(pre[i-self.synthesis.dna.rna_start], mutated)
                        item.moveBy(i*20+10, 80)
                        self.scene.addItem(item)
                        letter = QLabel()
                        letter.setAutoFillBackground(True)
                        letter.setStyleSheet("background-color: rgba(1, 0, 0, 0)")
                        letter.setText(pre[i-self.synthesis.dna.rna_start].upper())
                        letter.move(i*20+16, 80)
                        self.scene.addWidget(letter)
                else:
                    if i <= intronStart and i-intronStart < len(pre)-4:
                        item = IntronGraphicsItem(pre[i - self.synthesis.dna.rna_start], mutated)
                        item.moveBy(i * 20 + 10, 80)
                        self.scene.addItem(item)
                        letter = QLabel()
                        letter.setAutoFillBackground(True)
                        letter.setStyleSheet("background-color: rgba(1, 0, 0, 0)")
                        letter.setText(pre[i - self.synthesis.dna.rna_start].upper())
                        letter.move(i * 20 + 16, 80)
                        self.scene.addWidget(letter)
                    else:
                        item = RNAGraphicsItem(pre[i-self.synthesis.dna.rna_start], mutated)
                        item.moveBy(i*20+10, 80)
                        self.scene.addItem(item)
                        letter = QLabel()
                        letter.setAutoFillBackground(True)
                        letter.setStyleSheet("background-color: rgba(1, 0, 0, 0)")
                        letter.setText(pre[i-self.synthesis.dna.rna_start].upper())
                        letter.move(i*20+16, 80)
                        self.scene.addWidget(letter)

            item = DNAGraphicsItem(dna[i])
            item.moveBy(i*20+10, 96)
            self.scene.addItem(item)
            base = QLabel()
            base.setAutoFillBackground(True)
            base.setStyleSheet("background-color: rgba(1, 0, 0, 0)")
            base.setText(dna[i].upper())
            base.move(i*20+16, 102)
            self.scene.addWidget(base)

        i = 0
        mutated = False
        for i in range(len(rna)):
            item = RNAGraphicsItem(rna[i], mutated)
            item.moveBy(i*20+10, 280)
            self.scene.addItem(item)
            letter = QLabel()
            letter.setAutoFillBackground(True)
            letter.setStyleSheet("background-color: rgba(1, 0, 0, 0)")
            letter.setText(rna[i].upper())
            letter.move(i*20+16, 280)
            self.scene.addWidget(letter)
        i = 0
        for p in self.synthesis.peptide_chain.getChain():
            item = PeptideGraphicsItem()
            item.moveBy(i*60+10, 301)
            brush = QtGui.QBrush(1)
            brush.setColor(PeptideGraphicsItem.peptideColors[p])
            item.setBrush(brush)
            self.scene.addItem(item)
            name = QLabel()
            name.setAutoFillBackground(True)
            name.setStyleSheet("background-color: rgba(1, 0, 0, 0); font: 10pt")
            name.setText(p)
            if p in "Ochre, Amber, Opal":
                name.move(i*60+23, 322)
            else:
                name.move(i*60+29, 322)
            self.scene.addWidget(name)
            i += 1

        self.setScene(self.scene)
        self.show()

