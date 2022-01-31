import unittest

from protein_synthesis import ProteinSynthesis
from exception import InvalidDNASequence, EmptyRnaException


class TestProteinSynthesis(unittest.TestCase):
    def setUp(self):
        self.filename = "src/tests/test.txt"
        self.synthesis = ProteinSynthesis(self.filename,"0")
        self.synthesis.run_protein_synthesis()
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

    def test_DNA(self):
        self.assertEqual(self.synthesis.dna.getDNA(),self.dna_seq)

    def test_RNA(self):
        self.assertEqual(self.synthesis.rna.getPremRNA(),self.right_rna_seq)

    def test_peps(self):
        self.assertEqual(self.synthesis.peptide_chain.getChain(), ['Met', 'Asp', 'Ochre'])

    def test_empty_file(self):
        with self.assertRaises(InvalidDNASequence):
            p = ProteinSynthesis("src/tests/empty.txt", "")
            p.run_protein_synthesis()

    def test_os_error(self):
        with self.assertRaises(OSError):
            p = ProteinSynthesis("mau.txt", "")
            p.run_protein_synthesis()
