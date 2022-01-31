import unittest

from rna import RNA
from exception import InvalidDNASequence


class TestRNA(unittest.TestCase):

    def setUp(self):
        self.dna_seq = "taccattaacccgcggaagcattcctaatt"
        self.right_rna_seq = "augguaauugggcgccuucguaaggauuaa"
        self.right_exon = "auggauuaa"

    def test_create_rna(self):
        rna = RNA(self.dna_seq, "0")
        self.assertEqual(rna.getPremRNA(), self.right_rna_seq)

    def test_exon(self):
        """Tests remove intron."""
        rna = RNA(self.dna_seq, "0")
        self.assertEqual(rna.getRNA(), self.right_exon)

    def test_wrong_dna(self):
        with self.assertRaises(InvalidDNASequence):
            RNA("123", "0")

    def test_mutation(self):
        rna = RNA(self.dna_seq, "1")
        self.assertNotEqual(rna.getPremRNA(), self.right_rna_seq)
