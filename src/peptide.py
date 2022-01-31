from exception import InvalidDNASequence


class Peptide:
    """Class for peptide chains, which include many peptides.
    :parameter (string) RNA sequence."""

    peptides = {"uuu": "Phe", "uuc": "Phe", "uua": "Leu", "uug": "Leu",
                "cuu": "Leu", "cuc": "Leu", "cua": "Leu", "cug": "Leu",
                "auu": "Ile", "auc": "Ile", "aua": "Ile", "aug": "Met",
                "guu": "Val", "guc": "Val", "gua": "Val", "gug": "Val",
                "ucu": "Ser", "ucc": "Ser", "uca": "Ser", "ucg": "Ser",
                "ccu": "Pro", "ccc": "Pro", "cca": "Pro", "ccg": "Pro",
                "acu": "Thr", "acc": "Thr", "aca": "Thr", "acg": "Thr",
                "gcu": "Ala", "gcc": "Ala", "gca": "Ala", "gcg": "Ala",
                "uau": "Tyr", "uac": "Tyr", "uaa": "Ochre", "uag": "Amber",
                "cau": "His", "cac": "His", "caa": "Gln", "cag": "Gln",
                "aau": "Asn", "aac": "Asn", "aaa": "Lys", "aag": "Lys",
                "gau": "Asp", "gac": "Asp", "gaa": "Glu", "gag": "Glu",
                "ugu": "Cys", "ugc": "Cys", "uga": "Opal", "ugg": "Trp",
                "cgu": "Arg", "cgc": "Arg", "cga": "Arg", "cgg": "Arg",
                "agu": "Ser", "agc": "Ser", "aga": "Arg", "agg": "Arg",
                "ggu": "Gly", "ggc": "Gly", "gga": "Gly", "ggg": "Gly"}

    def __init__(self, rna_seq):
        self.peptideChain = []
        self.rna = rna_seq
        self.createPeptide()

    def getChain(self):
        return self.peptideChain

    def recognizePeptide(self, codon):

        if codon in self.peptides:
            return self.peptides[codon]
        else:
            raise InvalidDNASequence("Invalid codon.")

    def createPeptide(self):

        i = 0
        while i < len(self.rna):
            self.peptideChain.append(self.recognizePeptide(self.rna[i:i+3]))
            if self.rna[i:i+3] in {"uaa", "uag", "uga"}:
                break
            i += 3
