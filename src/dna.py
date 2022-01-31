from rna import RNA
from exception import InvalidDNASequence, EmptyRnaException


class DNA:

    def __init__(self, filename):
        self.dna_seq = None
        self.createDNA(filename)
        self.rna_start = 0
        self.rna_min_length = 10

    def createDNA(self, filename):

        # open file
        content = open(filename, "r").read().lower().replace("\n", "")

        # find place to start from
        index = content.find("tata")
        if index == -1:
            raise InvalidDNASequence("No TATA-box found in the given sequence.")
        try:
            self.dna_seq = content[index+4:-1]
        except IndexError:
            raise InvalidDNASequence("Empty file.")

    def getDNA(self):
        return self.dna_seq

    def createRNA(self, mutation_rate):

        i = 0
        while i < len(self.dna_seq):

            if self.dna_seq[i:i+3] == "tac":
                self.rna_start = i
                break
            else:
                i += 1   # codons are specific to mRNA not DNA

        temp = self.dna_seq[i:-1]

        i = 0
        end = 0
        while i < len(temp):
            if temp[i:i+3] == "att":
                if i > self.rna_min_length:
                    end = i
                    break
            elif temp[i:i+3] == "atc":
                if i > self.rna_min_length:
                    end = i
                    break
            elif temp[i:i+3] == "act":
                if i > self.rna_min_length:
                    end = i
                    break
            i += 3

        rna_seq = temp[:end+3]
        if rna_seq is None or len(rna_seq) == 0:
            raise EmptyRnaException("Empty RNA - please pick another file.")

        return RNA(rna_seq, mutation_rate)
