### Wichtige Libraries, die importiert werden müssen ###
import numpy as np
import streamlit as st
from io import StringIO


### Objektorientierte Programmierung mit Klassen ###

# Hauptklasse FASTA definieren
class FASTA:
    def __init__(self, fasta_input=""):
        self.fasta_input = fasta_input
        self.fasta_seq = ""
        self.fasta_header = ""
        self.fasta_inverted = ""
        self.fasta_base_counts = {}

    def fasta_file_to_string(self):
        self.fasta_input = self.fasta_input.getvalue().decode("utf-8")

    # Methode zum Aufreinigen eines FASTA-Textes zum Erzeugen eines Sequenz-Strings
    def get_sequence(self):
        lines = self.fasta_input.splitlines()                                                   # Der eingegebene Text wird in separate Lines gesplittet
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]                # Entfernung des Headers 
        self.fasta_seq = "".join(seq_lines).replace(" ", "").upper()                            # Die Linien werden in eine Sequenz gemerget und (falls nötig) in Großbuchstaben umgewandelt, Leerzeichen zwischen den Zeilen werden entfernt
    
    # Methode zur Extraktion der Header Zeilen
    def get_header(self):
        lines = self.fasta_input.splitlines()                                                   # Der eingegebene Text wird in separate Lines gesplittet
        self.fasta_header = [line.strip() for line in lines if line.startswith(">")]            # Entfernung aller Zeilen außer dem Header
           
    # Methode zur Erzeugung eines inversen DNA-Strangs in 5'-3'-Richtung
    def invert_sequence(self):
        sequence = self.fasta_seq                                                               # Abgreifen des Attributs für den Sequenz-String
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}                                   # Definition der komplementären Basen
        self.fasta_inverted = "".join(complement[base] for base in reversed(sequence))          # Umkehrung der Sequenz und Ersetzung der Basen durch ihre Komplementäre
            
    # Methode zum Zählen der Basen in der eingegebenen Sequenz
    def base_count(self):
        sequence = self.fasta_seq                                                               # Abgreifen des Attributs für den Sequenz-String
        self.fasta_base_counts = {base: sequence.count(base) for base in "ATCG"}                # Zählen der Basen in der Sequenz
        


### Aufbau der App-Page ###
# Titel der Seite
st.title("Analyze FASTA-DNA-Sequences")

# Sidebar für die Auswahl der gewünschten Funktionen
st.sidebar.title("Options")
fasta_file_on = st.sidebar.toggle("FASTA-Sequenz aus Datei laden", False)                       # Toggle-Button für die primäre Auswahl zwischen Text-Eingabe oder Datei-Upload
invert_DNA_on = st.sidebar.toggle("Inversen DNA-Strang anzeigen", False)                        # Toggle-Button für die Anzeige des inversen DNA-Strangs




### Prüfung auf Upload und konsekutivem Erstellen eines Objekts der Klasse FASTA ###
if fasta_file_on:
    file_uploaded = st.sidebar.file_uploader(                                                   # Sidebar-Datei-Upload für FASTA-Dateien
        "Drag and drop your file here:",
        type=["fasta", "fa", "mpfa", "fna", "fsa"]
        )

    if file_uploaded is not None:                                                               # Prüfung, ob eine Datei hochgeladen wurde
        FASTA_file = FASTA(file_uploaded)                                                       # Erstellen eines FASTA-Objekts mit der hochgeladenen Datei
        
        FASTA_file.fasta_file_to_string()                                                       # Das hochgeladene FASTA-File wird in einen String umgewandelt und intern gespeichert
        FASTA_file.get_sequence()                                                               # Aufruf der Methode zum Extrahieren der Sequenz aus dem FASTA-String
        FASTA_file.get_header()                                                                 # Aufruf der Methode zum Herausziehen des Headers


        ## Layout der ersten Spalte und der Anzeige des Sequenz-Headers darüber ##
        st.write(f"Header of the FASTA-Sequence: {FASTA_file.fasta_header}")                    # Ausgabe des Headers, der im Objekt FASTA-file gespeichert ist

        col1, col2 = st.columns(2)
        col1.header("Original")                                                                 # Header der Spalte
        col1.expander("DNA Sequence", True).write(FASTA_file.fasta_seq)                         # Anzeige der nativen Sequenz in der ersten (linken) Spalte


############################################### Bis hier hin überarbeitet ####################################################

    # Ausgabe der nativen Sequenz bei erfolgreichem Upload einer FASTA-Datei
    #if FASTA_file is not None:
        
    if invert_DNA_on and FASTA_file is not None:
        col2.header("Inverted DNA-Sequence")                                                              # Header für die Spalte mit der inversen Sequenz
        sequence_invert = FASTA(fasta_obj_file).sequence_invert()                                           # Aufruf der Methode zum Erzeugen der inversen Sequenz, falls der Toggle-Button aktiviert ist
        col2.write(f"Die inverse DNA-Sequenz lautet: {sequence_invert}")                                # Ausgabe der inversen Sequenz, falls der Toggle-Button aktiviert ist
    
else:
    fasta_seq_input = st.text_area("Gib deine FASTA-DNA-Sequenz manuell ein:")
    if fasta_seq_input:
        col1.header("Original DNA-Sequence")
        fasta_obj_input = FASTA(fasta_seq_input)
        header = fasta_obj_input.header_input()                                                                   # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Headers
        col1.write(f"Die Header-Zeile der DNA-Sequenz lautet: {header}")                                  # Ausgabe des Headers, der in der hochgeladenen Datei enthalten ist
        sequence_native = fasta_obj_input.sequence_input()                                                        # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Textes
        col1.write(f"Die Datei enthält folgende DNA-Sequenz: {sequence_native}") 
        #st.write(f"Die Datei enthält folgende DNA-Sequenz: {fasta_seq_input}")

    # Abfrage, ob die Sequenz invertiert werden soll
    if invert_DNA_on and fasta_seq_input:
        sequence_invert = FASTA(fasta_seq_input).sequence_invert()                                      # Aufruf der Methode zum Erzeugen der inversen Sequenz, falls der Toggle-Button aktiviert ist
        st.write(f"Die inverse DNA-Sequenz lautet: {sequence_invert}")                                  # Ausgabe der inversen Sequenz, falls der Toggle-Button aktiviert ist