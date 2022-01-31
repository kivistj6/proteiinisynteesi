from random import random, randint, seed
from time import time
from exception import InvalidDNASequence


class RNA:

    bases = {"a": "u", "t": "a", "c": "g", "g": "c"}

    def __init__(self, dna_seq: str, mutation_rate):
        self.rna_seq = None
        self.pre_rna = None
        self.intron_start = 0
        self.intron_end = 0
        self.faulty_reads = set()
        self.dna_seq = dna_seq
        self.createRNA(dna_seq, mutation_rate)
        self.removeInrtons()

    def getRNA(self):
        return self.rna_seq

    def getPremRNA(self):
        return self.pre_rna

    def removeInrtons(self):

        i = 3
        k = False
        while i < len(self.pre_rna)-1:
            if self.pre_rna[i:i+2] == "gu":
                self.intron_start = i
                k = True
                break
            i += 3

        l = False
        if self.intron_start != 0:
            j = self.intron_start+3
            while j < len(self.pre_rna)-4:
                if self.pre_rna[j+1:j+3] == "ag":
                    self.intron_end = j+3
                    l = True
                j += 3

        if l and k:
            self.rna_seq = self.pre_rna[0:self.intron_start] + self.pre_rna[self.intron_end:]

        elif not l and not k:
            self.rna_seq = self.pre_rna

    def createRNA(self, dna_seq, mutation_rate):

        i = 0
        temp = ""
        while i < len(dna_seq):
            if self.dna_seq[i] in self.bases:
                temp += self.bases[dna_seq[i]]
                i += 1

            else:
                raise InvalidDNASequence("Faulty lettering in DNA sequence.")

        self.pre_rna = temp
        self.mutate(mutation_rate)

    def mutate(self, rate):
        seed(time())
        if len(rate) == 0:
            return
        try:
            rate = float(rate)
        except ValueError:
            print("Error rate not a number")
            return
        for i in range(len(self.pre_rna)):
            if rate >= random():
                rna_types = ["a", "u", "c", "g"]
                rand = randint(0, 3)
                while self.pre_rna[i] == rna_types[rand]:
                    rand = randint(0, 3)
                self.pre_rna = self.pre_rna[:i]+rna_types[int(rand)]+self.pre_rna[i+1:]
                self.faulty_reads.add(i)
