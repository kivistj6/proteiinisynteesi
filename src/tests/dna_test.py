import unittest

from dna import DNA
from exception import InvalidDNASequence, EmptyRnaException


class TestDNA(unittest.TestCase):
    def setUp(self):
        self.filename = "src/tests/test.txt"
        self.dna_seq = "cgccgacaaaataaaccagccatgcgtaccattaacccgcggaagcattcctaat"+\
                       "tgcggcctcagtctatgcgtgccttggtgagaactttaggtaaaagataactgtctaa"+\
                       "ccgtgtccttgctcgaatgacagcaaagcaaggccacaatcgctagattcggcgatcg"+\
                       "cgcagtgattacatttgatgatagaggtactctgtgcaccctaccaggaggcctctat"+\
                       "caattagcattaagaccctgtcagacagtacgatcatatcctccagcttctgatggtc"+\
                       "agggactgcgagcccaactgtcccatccacacgttagttggtgcgcctgacccaaatg"+\
                       "ctggggagtggccgttgtacaacgtggatgggtccgaggcgttgcacgttccgagttt"+\
                       "attacgcttgtgggttatacgctccgggaacttcgtgtttcctggatttctccccagc"+\
                       "cccttccatagcccactcatttctgacgagatgatggacctatccgccaccatagaacc"+\
                       "tgaacctgagtaccccagataccggtttaatagaacttagtcacgatgtgatggcgacc"+\
                       "ggatctaaagctggctggcgagactttagggtttgtgtgaccacttacgcctgggtacg"+\
                       "gcggtcgactgatatcatatgctttgcaggggcgtcgata"
        self.right_rna_seq = "augguaauugggcgccuucguaaggauuaa"

    def test_create_dna(self):
        dna = DNA(self.filename)
        self.assertEqual(self.dna_seq,dna.getDNA())

    def test_create_rna(self):
        rna = DNA(self.filename).createRNA("0")
        self.assertEqual(rna.getPremRNA(),self.right_rna_seq)

    def test_faulty_file(self):
        with self.assertRaises(OSError):
            DNA("jasdf")

    def test_empty_file(self):
        with self.assertRaises(InvalidDNASequence):
            DNA("src/tests/empty.txt")

    def test_invalid_file(self):
        with self.assertRaises(InvalidDNASequence):
            DNA("src/tests/invalid file.txt")

    def test_no_rna(self):
        dna = DNA(self.filename)
        dna.dna_seq = ""
        with self.assertRaises(EmptyRnaException):
            dna.createRNA("0")
