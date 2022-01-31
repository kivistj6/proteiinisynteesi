from dna import DNA
from peptide import Peptide
from exception import InvalidDNASequence, EmptyRnaException


class ProteinSynthesis:
    """Class for running protein synthesis. Requires .txt filename and (int) error rate as inputs."""

    def __init__(self, filename, error):
        self.filename = filename
        self.error_rate = error
        self.dna = None
        self.rna = None
        self.peptide_chain = None

    def run_protein_synthesis(self):
        """ Used for running the synthesis. Uses DNA, RNA & Peptide classes for its functionality.
        :raises InvalidDNASequence or EmptyRnaException if file is not right.
        :raises OSError if there is problem with file reading."""

        try:
            self.dna = DNA(self.filename)
            self.rna = self.dna.createRNA(self.error_rate)
            rna_seq = self.rna.getRNA()
            if rna_seq is None or len(rna_seq) < 3:
                raise EmptyRnaException("Mutation ate all the exons. Please, try again.")
            self.peptide_chain = Peptide(rna_seq)

        except OSError as e:
            print(e)
            raise e
        except InvalidDNASequence as e:
            print(e)
            raise e
        except EmptyRnaException as e:
            print(e)
            raise e
        except Exception as e:
            print(e)
            raise e
