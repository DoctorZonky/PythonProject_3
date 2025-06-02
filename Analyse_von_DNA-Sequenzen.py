##### Projekt 3: Analyse von DNA-Sequenzen ####

# Installation aller wichtigen Libraries
import streamlit as st
import numpy as np

# Hauptklasse definieren
class FASTA:
    def __init__(self, fasta_text):
        self.fasta_text = fasta_text

    # Funktion, die nur die DNA-Sequenz aus der FASTA-Datei extrahiert und den Header ignoriert
    def fasta_input(self):
        lines = self.fasta_text.splitlines()
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]
        sequence = "".join(seq_lines).replace(" ", "").upper()
        return sequence


st.title("Analyze FASTA-DNA-Sequences")

fasta_data_on = st.toggle("FASTA aus Datei laden", False)

if fasta_data_on:
    fasta_extensions = ["fasta", "fa", "mpfa", "fna", "fsa"]
    fasta_file = st.file_uploader("Lade hier deine FASTA-Datei hoch:", type=fasta_extensions)
    
    st.write(f"Die Datei enthält folgende DNA-Sequenz: {FASTA.fasta_input(fasta_file)}")
    
else:
    fasta_seq_input = st.text_input("Gib deine FASTA-DNA-Sequenz manuell ein:")
    st.write(f"Die eingegebene DNA-Sequenz lautet: {fasta_seq_input}")