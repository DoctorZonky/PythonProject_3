

class FASTA(self, fasta_text):
    def __init__(self, fasta_text = ""):
        self.fasta_text_raw = fasta_text
        self.fasta_text = ""
        self.fasta_inverted = ""
        self.fasta_base_count = {}

    def fasta_input(self):
        lines = self.fasta_text_raw.splitlines()
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]
        sequence = "".join(seq_lines).replace(" ", "").upper()
        
        return sequence
    
    def fasta_invert(self):
        sequence = self.fasta_text
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        inverted_sequence = "".join(complement[base] for base in reversed(sequence))
        return inverted_sequence
    
    def fasta_base_count(self):
        sequence = self.fasta_text
        base_counts = {base: sequence.count(base) for base in "ATCG"}
        return base_counts