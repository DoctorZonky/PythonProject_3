### Wichtige Libraries, die importiert werden müssen ###
import numpy as np
import streamlit as st
from io import StringIO


### Objektorientierte Programmierung mit Klassen ###

# Hauptklasse FASTA definieren
class FASTA:
    def __init__(self, fasta_text=""):
        self.fasta_text = fasta_text

    # Funktion zum Upload eines Files und Speichern in einer Variable
    def upload_FASTA_file(self):
        fasta_extensions = ["fasta", "fa", "mpfa", "fna", "fsa"]
        FASTA_file = st.file_uploader("Lade hier deine FASTA-Datei hoch:", type=fasta_extensions)       # Hier wird die Datei hochgeladen und als Variable gespeichert
        return FASTA_file                                                                               # Ausgabe der Fasta-Datei

    # Methode zum Aufreinigen eines FASTA-Textes zum Erzeugen eines Sequenz-Strings
    def sequence_input(self):
        lines = self.fasta_text.splitlines()                                                            # Der eingegebene Text wird in separate Lines gesplittet
        seq_lines = [line.strip() for line in lines if not line.startswith(">")]                        # Entfernung des Headers 
        sequence = "".join(seq_lines).replace(" ", "").upper()                                          # Die Linien werden in eine Sequenz gemerget und (falls nötig) in Großbuchstaben umgewandelt, Leerzeichen zwischen den Zeilen werden entfernt
        return sequence
    
    # Methode zur Extraktion der Header Zeilen
    def header_input(self):
        lines = self.fasta_text.splitlines()                                                            # Der eingegebene Text wird in separate Lines gesplittet
        header = [line.strip() for line in lines if line.startswith(">")]                               # Entfernung aller Zeilen außer dem Header
        return header
    
    # Methode zur Erzeugung eines inversen DNA-Strangs in 5'-3'-Richtung
    def sequence_invert(self):
        sequence = self.sequence_input()                                                                # Aufruf der Methode zum Aufreinigen des FASTA-Textes
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}                                           # Definition der komplementären Basen
        inverted_sequence = "".join(complement[base] for base in reversed(sequence))                    # Umkehrung der Sequenz und Ersetzung der Basen durch ihre Komplementäre
        return inverted_sequence
    
    # Methode zum Zählen der Basen in der eingegebenen Sequenz
    def base_count(self):
        sequence = self.sequence_input()                                                                # Aufruf der Methode zum Aufreinigen des FASTA-Textes
        base_counts = {base: sequence.count(base) for base in "ATCG"}                                   # Zählen der Basen in der Sequenz
        return base_counts



### Aufbau der App-Page ###
# Titel der Seite
st.title("Analyze FASTA-DNA-Sequences")

# Sidebar für die Auswahl der gewünschten Funktionen
st.sidebar.title("Button-Auswahl")
fasta_file_on = st.sidebar.toggle("FASTA-Sequenz aus Datei laden", False)                               # Toggle-Button für die primäre Auswahl zwischen Text-Eingabe oder Datei-Upload
invert_DNA_on = st.sidebar.toggle("Inversen DNA-Strang anzeigen", False)                                # Toggle-Button für die Anzeige des inversen DNA-Strangs

# Spalten-Layout für die Anzeige der Ergebnisse
col1, col2 = st.columns(2)                                                                              # Erstellen von zwei Spalten für die Anzeige der Ergebnisse


### Prüfung auf Upload und konsekutivem Erstellen eines Objekts der Klasse FASTA ###
if fasta_file_on:
    FASTA_file = FASTA().upload_FASTA_file()                                                            # Erstellen eines Objekts und Aufruf der Funktion zum Hochladen einer Datei

    # Ausgabe der nativen Sequenz bei erfolgreichem Upload einer FASTA-Datei
    if FASTA_file is not None:
        col1.header("Original DNA-Sequence")
        fasta_text = FASTA_file.getvalue().decode("utf-8")                                              # Die Datei wird in einen String umgewandelt
        header = FASTA(fasta_text).header_input()                                                       # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Headers
        col1.write(f"Die Header-Zeile der DNA-Sequenz lautet: {header}")                                # Ausgabe des Headers, der in der hochgeladenen Datei enthalten ist
        sequence_native = FASTA(fasta_text).sequence_input()                                            # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Textes
        col1.write(f"Die Datei enthält folgende DNA-Sequenz: {sequence_native}")                        # Ausgabe der Sequenz, die in der hochgeladenen Datei enthalten ist


    if invert_DNA_on and FASTA_file is not None:
        col2.header("Inverted DNA-Sequence")                                                              # Header für die Spalte mit der inversen Sequenz
        sequence_invert = FASTA(fasta_text).sequence_invert()                                           # Aufruf der Methode zum Erzeugen der inversen Sequenz, falls der Toggle-Button aktiviert ist
        col2.write(f"Die inverse DNA-Sequenz lautet: {sequence_invert}")                                # Ausgabe der inversen Sequenz, falls der Toggle-Button aktiviert ist
    
else:
    fasta_seq_input = st.text_area("Gib deine FASTA-DNA-Sequenz manuell ein:")
    if fasta_seq_input:
        col1.header("Original DNA-Sequence")
        fasta_obj = FASTA(fasta_seq_input)
        header = fasta_obj.header_input()                                                                   # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Headers
        col1.write(f"Die Header-Zeile der DNA-Sequenz lautet: {header}")                                  # Ausgabe des Headers, der in der hochgeladenen Datei enthalten ist
        sequence_native = fasta_obj.sequence_input()                                                        # Erstellen eines Objekts der Klasse FASTA und Aufruf der Methode zum Aufreinigen des Textes
        col1.write(f"Die Datei enthält folgende DNA-Sequenz: {sequence_native}") 
        #st.write(f"Die Datei enthält folgende DNA-Sequenz: {fasta_seq_input}")

    # Abfrage, ob die Sequenz invertiert werden soll
    if invert_DNA_on and fasta_seq_input:
        sequence_invert = FASTA(fasta_seq_input).sequence_invert()                                      # Aufruf der Methode zum Erzeugen der inversen Sequenz, falls der Toggle-Button aktiviert ist
        st.write(f"Die inverse DNA-Sequenz lautet: {sequence_invert}")                                  # Ausgabe der inversen Sequenz, falls der Toggle-Button aktiviert ist

