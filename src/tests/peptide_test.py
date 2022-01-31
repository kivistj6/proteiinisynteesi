import unittest

from peptide import Peptide
from exception import InvalidDNASequence


class TestPeptide(unittest.TestCase):

    def setUp(self):
        self.rna_seq = "auggauuaa"
        self.peps = Peptide(self.rna_seq)

    def test_create_peptide(self):
        self.assertEqual(self.peps.getChain(), ['Met', 'Asp', 'Ochre'])

    def test_codon_mistake(self):
        with self.assertRaises(InvalidDNASequence):
            self.peps.recognizePeptide("codonite")
